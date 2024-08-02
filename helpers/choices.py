from django.utils.translation import gettext_lazy as _


class ModelChoices:

    NIGERIAN_STATES = (
        ('Abia', _('Abia')),
        ('Adamawa', _('Adamawa')),
        ('Akwa Ibom', _('Akwa Ibom')),
        ('Anambra', _('Anambra')),
        ('Bauchi', _('Bauchi')),
        ('Bayelsa', _('Bayelsa')),
        ('Benue', _('Benue')),
        ('Borno', _('Borno')),
        ('Cross River', _('Cross River')),
        ('Delta', _('Delta')),
        ('Ebonyi', _('Ebonyi')),
        ('Edo', _('Edo')),
        ('Ekiti', _('Ekiti')),
        ('Enugu', _('Enugu')),
        ('FCT', _('Federal Capital Territory')),
        ('Gombe', _('Gombe')),
        ('Imo', _('Imo')),
        ('Jigawa', _('Jigawa')),
        ('Kaduna', _('Kaduna')),
        ('Kano', _('Kano')),
        ('Katsina', _('Katsina')),
        ('Kebbi', _('Kebbi')),
        ('Kogi', _('Kogi')),
        ('Kwara', _('Kwara')),
        ('Lagos', _('Lagos')),
        ('Nasarawa', _('Nasarawa')),
        ('Niger', _('Niger')),
        ('Ogun', _('Ogun')),
        ('Ondo', _('Ondo')),
        ('Osun', _('Osun')),
        ('Oyo', _('Oyo')),
        ('Plateau', _('Plateau')),
        ('Rivers', _('Rivers')),
        ('Sokoto', _('Sokoto')),
        ('Taraba', _('Taraba')),
        ('Yobe', _('Yobe')),
        ('Zamfara', _('Zamfara')),
    )

    LOCAL_GOV = (
        ('Abeokuta North', _('Abeokuta North')),
        ('Abeokuta South', _('Abeokuta South')),
        ('Ado Odo-ota', _('Ado Odo-ota')),
        ('Ewekoro', _('Ewekoro')),
        ('Ifo', _('Ifo')),
        ('Ijebu East', _('Ijebu East')),
        ('Ijebu North', _('Ijebu North')),
        ('Ijebu North East', _('Ijebu North East')),
        ('Ijebu Ode', _('Ijebu Ode')),
        ('Ikenne', _('Ikenne')),
        ('Imeko Afon', _('Imeko Afon')),
        ('Ipokia', _('Ipokia')),
        ('Obafemi Owode', _('Obafemi Owode')),
        ('Odeda', _('Odeda')),
        ('Odogbolu', _('Odogbolu')),
        ('Ogun Water Side', _('Ogun Water Side')),
        ('Remo North', _('Remo North')),
        ('Sagamu', _('Sagamu')),
        ('Yewa North', _('Yewa North')),
        ('Yewa South', _('Yewa South')),
    )

    GENDER = (
        ('male', _('Male')),
        ('female', _('Female'))
    )

    BOOL_CHOICES = (
        ('True', _('Yes')),
        ('False', _('No'))
    )

    
