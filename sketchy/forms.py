from . import parser, models
from django import forms


class ParserContainer(forms.Form):
    MEDIA_CHOICE = (
        ("Contents", "Contents"),
        ("Contents2", "Contents2")
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            "media_type"
        ]

    def parse_data(self):
        if self.data["media_type"] == "Contents":
            content_parser = parser.parser_func()
            for i in content_parser:
                models.Content.objects.create(**i)
        elif self.data["media_type"] == "Contents2":
            content_parser2 = parser.parser_func()
            for i in content_parser2:
                models.Content.objects.create(**i)



