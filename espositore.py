class Espositore:
    def _init_(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome

    def _eq_(self, other):
        if isinstance(other, Espositore):
            return self.codice == other.codice
        return False

    def _str_(self):
        return f"{self.codice}: {self.nome} {self.cognome}"