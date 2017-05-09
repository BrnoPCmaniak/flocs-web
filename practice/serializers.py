from rest_framework import serializers
from flocs.student_extractors import get_student_level, get_active_credits
from flocsweb.store import db_state
from .models import Student, TaskSession


class TaskSessionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TaskSession
        fields = ('url', 'task_session_id', 'student', 'task', 'solved', 'given_up',
                  'start', 'end')

        extra_kwargs = {
            'url': {'view_name': 'task_session-detail'},
        }

    def validate(self, data):
        """
        Check that the task is not solved and given up at the same time.
        """
        if data['solved'] and data['given_up']:
            raise serializers.ValidationError("A task cannot be solved and given up at the same time.")
        return data


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    level = serializers.SerializerMethodField()
    active_credits = serializers.SerializerMethodField()
    seen_instructions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    practice_overview = serializers.HyperlinkedIdentityField(
        view_name='student-practice-overview',
        read_only=True)
    edit_program = serializers.HyperlinkedIdentityField(
        view_name='student-edit-program',
        read_only=True)
    run_program = serializers.HyperlinkedIdentityField(
        view_name='student-run-program',
        read_only=True)

    class Meta:
        model = Student

    def get_active_credits(self, student):
        return get_active_credits(db_state, student_id=student.student_id)

    def get_level(self, student):
        return get_student_level(db_state, student_id=student.student_id).level_id


class StudentInstructionSerializer(serializers.Serializer):
    instruction_id = serializers.CharField()
    seen = serializers.BooleanField()


class StudentTaskSerializer(serializers.Serializer):
    task_id = serializers.CharField()
    solved = serializers.BooleanField()
    time = serializers.DurationField()


class RecommendationSerializer(serializers.Serializer):
    available = serializers.BooleanField()
    task_id = serializers.CharField()


class PracticeOverviewSerializer(serializers.Serializer):
    level = serializers.IntegerField()
    credits = serializers.IntegerField()
    active_credits = serializers.IntegerField()
    instructions = StudentInstructionSerializer(many=True)
    tasks = StudentTaskSerializer(many=True)
    recommendation = RecommendationSerializer()


class ProgressSerializer(serializers.Serializer):
    level = serializers.IntegerField()
    credits = serializers.IntegerField()
    active_credits = serializers.IntegerField()


class ProgramExecutionReportSerializer(serializers.Serializer):
    correct = serializers.BooleanField()
    progress = ProgressSerializer(required=False)
    recommendation = RecommendationSerializer(required=False)
