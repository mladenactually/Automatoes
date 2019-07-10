class ResourceAware:
    def __init__(self, **resources):
        self.electricity = resources.get('electricity', 0)
        self.water = resources.get('water', 0)
        self.internet = resources.get('internet', 0)
        self.gas = resources.get('gas', 0)


class ToggleSettings:
    def __init__(self, is_on=True):
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True

    def turn_on_for(self, duration):
        self.is_on = True

    def turn_on_in(self, delay):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def turn_off_for(self, duration):
        self.is_on = False

    def turn_off_in(self, delay):
        self.is_on = False


class ContinuousScale:
    def __init__(self, **minmax):
        self.min_value = minmax['min']
        self.max_value = minmax['max']
        self._value = self.min_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self.min_value <= new_value <= self.max_value:
            self._value = new_value
        else:
            raise ValueError(f'{new_value} out of range [{self.min_value}, {self.max_value}].')

    def adjust(self, new_value):
        self.value = new_value

    def adjust_for(self, new_value, duration):
        self.value = new_value
        # TODO: евентуално асинхроно поставити вредност, ако буде било вреемена ;).

    def adjust_in(self, new_value, delay):
        self.value = new_value
        # TODO: види горњи todo.


class DiscreteScale:
    def __init__(self, scale):
        if not scale:
            raise ValueError('scale must not be empty')
        scale.sort()
        self.scale = scale
        self._value = scale[0]

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value in self.scale:
            self._value = new_value
        else:
            raise ValueError(f'{new_value} not in range {self.scale}')

    def adjust(self, new_value):
        self.value = new_value

    def adjust_for(self, new_value, duration):
        self.value = new_value

    def adjust_in(self, new_value, delay):
        self.value = new_value


class SecuritySettings:
    def __init__(self, pin, is_set_off=False):
        self.pin = pin
        self.is_set_off = is_set_off

    def check_pin(self, pin):
        return self.pin == pin

    def notify(self):
        pass
        # TODO: имплементирати како треба. Како треба? Немам појма.

    def stop(self):
        pass
        # TODO: види горњи todo.


class Device:
    def __init__(self, name, **settings):
        self.usable = True
        self.name = name
        self.toggle_settings = settings.get('toggle_settings')
        self.resources = settings.get('resources')
        self.discrete_scale = settings.get('discrete_scale')
        self.continuous_scale = settings.get('continuous_scale')
        self.security_settings = settings.get('security_settings')
