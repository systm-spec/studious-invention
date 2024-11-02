class BaseCharacter:
    ## Konstruktor-Methode
    def __init__(self,name, gender, race, spec, strength = 0, stam=0, const = 0, ag= 0, vers=0, sav=0, mana=0, vol=0,wis=0, faith=0, hp=0,vig=0,hard=0,armor=0, ev=0, bl=0):
        # character info
        self.name = name              # Name
        self.gender = gender          # Gender
        self.race = race              # Rasse
        self.specialization = spec    # Klasse

        # physical
        self._strength = strength   # Physischer Schaden
        self._stamina = stam   # Physische Währung
        self._constitution = const   # Stärke-Regenrationsrate
        self._agility = ag   # Physisch-Krit DMG
        self._versatility = vers   # Physisch-Krit Rate

        # magical
        self._savvy = sav  # Magischer Schaden
        self._mana = mana   # Magische Währung
        self._volition = vol  # Mana-Regenrationsrate
        self._wisdom = wis  # Magie-Krit DMG
        self._faith = faith  # Magie-Krit Rate

        # hit points
        self._hitpoints = hp  #  Base HP
        self._vigour = vig  #  HP-Regen-Rate
        self._hardening = hard  # additional HP
        self._armor = armor  # Armor Items

        # Misc
        self._evade =ev  # Ausweischance
        self._block = bl  # Blockchance

    ## Destruktormethode
    def __del__(self):
        print(f"Objekt {self.name} removed.")

    ## Getter & Setter

    # Physicals
    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        self._strength = value

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        self._stamina = value

    @property
    def constitution(self):
        return self._constitution

    @constitution.setter
    def constitution(self, value):
        self._constitution = value

    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, value):
        self._agility = value

    @property
    def versatility(self):
        return self._versatility

    @versatility.setter
    def versatility(self, value):
        self._versatility = value

    # Magical
    @property
    def savvy(self):
        return self._savvy

    @savvy.setter
    def savvy(self, value):
        self._savvy = value

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = value

    @property
    def volition(self):
        return self._volition

    @volition.setter
    def volition(self, value):
        self._volition = value

    @property
    def wisdom(self):
        return self._wisdom

    @wisdom.setter
    def wisdom(self, value):
        self._wisdom = value

    @property
    def faith(self):
        return self._faith

    @faith.setter
    def faith(self, value):
        self._faith = value

    # Hit Points
    @property
    def hitpoints(self):
        return self._hitpoints

    @hitpoints.setter
    def hitpoints(self, value):
        self._hitpoints = value

    @property
    def vigour(self):
        return self._vigour

    @vigour.setter
    def vigour(self, value):
        self._vigour = value

    @property
    def hardening(self):
        return self._hardening

    @hardening.setter
    def hardening(self, value):
        self._hardening = value

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, value):
        self._armor = value

    # Misc Attributes
    @property
    def evade(self):
        return self._evade

    @evade.setter
    def evade(self, value):
        self._evade = value

    @property
    def block(self):
        return self._block

    @block.setter
    def block(self, value):
        self._block = value