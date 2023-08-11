from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

class SentimentAnalysis(Model):
    _id = fields.IntField(pk=True, index=True)
    text = fields.TextField(null=False)
    label = fields.IntField(null=False)

class SentimentAnalysis_FeedbackLoop(Model):
    _id = fields.IntField(pk=True, index=True)
    text = fields.TextField(null=False)
    label = fields.IntField(null=False)

class KeywordExtraction(Model):
    _id = fields.IntField(pk=True, index=True)
    text = fields.TextField(null=False)
    label = fields.TextField(null=False)

class KeywordExtraction_FeedbackLoop(Model):
    _id = fields.IntField(pk=True, index=True)
    text = fields.TextField(null=False)
    label = fields.TextField(null=False)

sentiment_analysis = pydantic_model_creator(SentimentAnalysis, name="SentimentAnalysis", exclude=("label"))
sentiment_analysisIn = pydantic_model_creator(SentimentAnalysis, name="SentimentAnalysisIn", exclude=("label"), exclude_readonly=True)
sentiment_analysisOut = pydantic_model_creator(SentimentAnalysis, name="SentimentAnalysisOut", exclude=("text"))
