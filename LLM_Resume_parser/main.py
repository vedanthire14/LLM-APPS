api_key = ''

from promptify import Prompter,OpenAI, Pipeline


model        = OpenAI(api_key) # or `HubModel()` for Huggingface-based inference or 'Azure' etc
prompter     = Prompter('ner.jinja') # select a template or provide custom template
pipe         = Pipeline(prompter , model)
