from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # len_name= serializers.SerializerMethodField()
    # custom_name= serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"




        #exclude =["active"]
    # def get_len_name(self,object):
    #     length=len(object.name)
    #     return length
    #  def get_custom_name(self,obect):
    #      return "Very Good"

    # def validate(self,data):
    #     if data["name"] ==data["description"]:
    #         raise serializers.ValidationError("Title and Description should be different")
    #     else:
    #         return data

    # def validate_name(self,value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Name is Too Sht")
    #     return value




#This is core validate

# def name_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError("Name is Too Sht")
#     return value

# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_length])
#     description=serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)


#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name' , instance.name)
#         instance.description=validated_data.get('description', instance.description)
#         instance.active=validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#         # This is object based validate

    # def validate(self,data):
    #     if data["name"] ==data["description"]:
    #         raise serializers.ValidationError("Title and Description should be different")
    #     else:
    #         data


#This is a field based validate

    # def validate_name(self,value):

    #     if len(value) < 3:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
