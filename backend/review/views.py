from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import permission_classes
from django.db import IntegrityError
from rest_framework.response import Response

from user.utils import get_user_by_name
from .models import *
from .serializers import *
from .permissions import *


class UserReviewOptionsDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'activity': Activity.objects.all().values_list('name', flat=True),
            'positive_keywords': UserReviewKeyword.objects.filter(type=ReviewKeywordType.POSITIVE).values_list(
                'content', flat=True),
            'negative_keywords': UserReviewKeyword.objects.filter(type=ReviewKeywordType.NEGATIVE).values_list(
                'content', flat=True)
        }
        return Response(data, status=status.HTTP_200_OK)


class UserReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = UserReviewCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({'detail': 'user can write review only once'}, status=status.HTTP_409_CONFLICT)


class IsEligibleForWritingReviewAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        reviewee = get_user_by_name(request.data.get('reviewee', ''))
        can_write = not reviewee.reviews.filter(reviewer=request.user).exists()
        return Response({'can_write': can_write}, status=status.HTTP_200_OK)


class UserReviewListAPIView(generics.ListAPIView):
    serializer_class = UserReviewDetailSerializer

    def get_queryset(self):
        name = self.kwargs.get('name', None)
        user = User.objects.get(name=name)
        return UserReview.objects.filter(reviewee=user)


@permission_classes([IsReviewer])
class UserReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserReviewCreateUpdateSerializer

    def initial(self, request, *args, **kwargs):
        self.review = get_object_or_404(UserReview, pk=self.kwargs.get('pk', None))
        super().initial(request, *args, **kwargs)

    def get_object(self):
        return self.review

    def patch(self, request, *args, **kwargs):
        if self.review.edited:
            return Response({'detail': 'user can edit review only once'}, status=status.HTTP_400_BAD_REQUEST)
        return super().patch(request, *args, **kwargs)


@permission_classes([IsReviewee])
class UserReviewCommentCreateAPIView(generics.CreateAPIView):
    serializer_class = UserReviewCommentCreateUpdateSerializer
    queryset = UserReviewComment.objects.all()

    def initial(self, request, *args, **kwargs):
        self.review = get_object_or_404(UserReview, pk=request.data.get('review', None))
        super().initial(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({'detail': 'user can comment only once'}, status=status.HTTP_409_CONFLICT)


@permission_classes([IsReviewee])
class UserReviewCommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserReviewCommentCreateUpdateSerializer
    queryset = UserReviewComment.objects.all()

    def initial(self, request, *args, **kwargs):
        self.comment = get_object_or_404(UserReviewComment, pk=self.kwargs.get('pk', None))
        self.review = self.comment.review
        super().initial(request, *args, **kwargs)

    def get_object(self):
        return self.comment

    def patch(self, request, *args, **kwargs):
        if self.comment.edited:
            return Response({'detail': 'User can edit comment only once'}, status=status.HTTP_400_BAD_REQUEST)
        return super().patch(request, *args, **kwargs)
