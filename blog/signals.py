from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_delete, pre_save, post_init, post_delete, post_save


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('Logged in hello')
    print('sender:', sender)
    print('request:', request)
    print('user:', user)
    print(f'Kwargs:{kwargs}')
    print('user  pass:', user.password)
    # user_logged_in.connect(login_success, sender=User)  not need if @@receiver(user_logged_in, sender=User) is written above


@receiver(user_logged_out, sender=User)
def logged_out(sender, request, user, **kwargs):
    print('Logged out tata')
    print('sender:', sender)
    print('request:', request)
    print('user:', user)
    print(f'Kwargs:{kwargs}')
    print('user  pass:', user.password)

    # user_logged_out.connect(logged_out, sender=User)  not need if @@receiver(user_logged_in, sender=User) is written above


@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwargs):
    print('Login_failed Upps')
    print('sender:', sender)
    print('request:', request)
    print('credentials:', credentials)

    print(f'Kwargs:{kwargs}')

    # user_logged_out.connect(login_failed)  not need if @@receiver(user_logged_in, sender=User) is written above


@receiver(pre_save, sender=User)
def beginin_save(sender, instance, **kwargs):

    print('pre_save signal')

    print('sender:', sender)

    print('instance:', instance)

    print(f'Kwargs:{kwargs}')

    # pre_save.connect(beginin_save, sender=User)


@receiver(post_save, sender=User)
def end_save(sender, instance, created, raw, using, update_fields, **kwargs):
    if created:

        print(' post_save created signal')

        print('sender:', sender)

        print('instance:', instance)

        print('created:', created)

        print('raw:', raw)

        print('using:', using)

        print('update_fields:', update_fields)

        print(f'Kwargs:{kwargs}')
    else:
        print(' post_save update signal')

        print('sender:', sender)

        print('instance:', instance)

        print('created:', created)

        print('raw:', raw)

        print('using:', using)

        print('update_fields:', update_fields)

        print(f'Kwargs:{kwargs}')

        # post_save.connect(end_save, sender=User)


@receiver(pre_delete, sender=User)
def at_begining_delete(sender, instance, using, **kwargs):
    print('pre_delete')
    print('sender:', sender)
    print('instance:', instance)
    print('using:', using)

    # pre_delete.connect(at_begining_delete, sender=User)  not need if @@receiver(user_logged_in, sender=User) is written above


@receiver(post_delete, sender=User)
def at_end_delete(sender, instance, using, **kwargs):
    print('Post_delete')
    print('sender:', sender)
    print('instance:', instance)
    print('using:', using)

    # post_delete.connect(at_end_delete, sender=User)  not need if @@receiver(user_logged_in, sender=User) is written above
