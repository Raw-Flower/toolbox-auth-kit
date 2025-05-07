from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
    
# Mixin class for avoid use cache from browser
@method_decorator(never_cache, name='dispatch')
class NeverBrowserCache(View):
    pass

# Mixin class for required authentication
class SecureView(LoginRequiredMixin, NeverBrowserCache):
    pass
