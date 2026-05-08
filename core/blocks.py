from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class StatBlock(blocks.StructBlock):
    value = blocks.CharBlock(max_length=20, help_text="e.g. 500+")
    label = blocks.CharBlock(max_length=100, help_text="e.g. Participants")
    
    class Meta:
        icon = "decimal"
        template = "blocks/stat_block.html"

class TimelineItemBlock(blocks.StructBlock):
    date = blocks.CharBlock(max_length=100)
    title = blocks.CharBlock(max_length=200)
    description = blocks.TextBlock(required=False)

    class Meta:
        icon = "date"

class TimelineBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    items = blocks.ListBlock(TimelineItemBlock())

    class Meta:
        icon = "list-ul"
        template = "blocks/timeline_block.html"

class BentoItemBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=200)
    text = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock(required=False)
    link = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)
    
    # Grid positioning / sizing
    size = blocks.ChoiceBlock(choices=[
        ('1x1', 'Small (1x1)'),
        ('2x1', 'Wide (2x1)'),
        ('1x2', 'Tall (1x2)'),
        ('2x2', 'Large (2x2)'),
    ], default='1x1')

    class Meta:
        icon = "doc-full"

class BentoGridBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    items = blocks.ListBlock(BentoItemBlock())

    class Meta:
        icon = "grip"
        template = "blocks/bento_grid_block.html"
