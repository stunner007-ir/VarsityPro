from rest_framework import views, status
from rest_framework.response import Response
from .tasks import summarize_text
from .serializers import SummarizeTextSerializer


class SummarizeTextView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = SummarizeTextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            task = summarize_text.delay(text)
            return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SummarizeResultView(views.APIView):
    def get(self, request, task_id, *args, **kwargs):
        from celery.result import AsyncResult
        result = AsyncResult(task_id)
        if result.state == 'PENDING':
            response = {'state': result.state}
        elif result.state != 'FAILURE':
            response = {
                'state': result.state,
                'result': result.result
            }
        else:
            response = {
                'state': result.state,
                'result': str(result.info)
            }
        return Response(response)
