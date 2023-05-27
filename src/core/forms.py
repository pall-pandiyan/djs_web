from django.forms.renderers import TemplatesSetting


class CustomFormRenderer(TemplatesSetting):
    form_template_name = "form_snippet.html"
