   from django.utils.translation import ugettext_lazy as _
   from oidc_provider.lib.claims import ScopeClaims

   def userinfo(claims, user):
       claims['name'] = f'{user.first_name} {user.last_name}'
       claims['given_name'] = user.first_name
       claims['family_name'] = user.last_name
       claims['email'] = user.email
       claims['address'] = {'street_address': '...'}
       return claims

