from django.conf import settings

import importlib

# Merge two lots of mesobox-compatible context additions
def merge_context_additions(additions):
    context = {}
    boxes = {}
    for c in additions:
        try:
            context.update(c.get("context"))
        except TypeError:
            pass
        try:
            for k, v in c.get("boxes").items():
                if k in boxes:
                    boxes[k].append(v)
                else:
                    boxes[k] = v
        except TypeError:
            pass
        except AttributeError:
            pass
    return {"context": context, "boxes": boxes}
        
def context_processor(request):
    additions = {}

    # Get the boxes and accompanying context additions from all the installed apps.
    for app in settings.INSTALLED_APPS:
        try:
            module = importlib.import_module(app+".boxes")
        except ImportError:
            continue
        # Run each function now.
        for b in module.BOX_INCLUDES:
            b_func = getattr(module, b)
            if not b_func:
                raise Exception("Method %s not implemented in module %s" % (b, app))
            additions = merge_context_additions([additions, b_func(request)])
    
    # Merge boxes down to being part of the context additions dict now they have all been assembled
    result = additions['context']
    result['boxes'] = additions['boxes']

    return result


