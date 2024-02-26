class ConvertBit:

    bitsunite = ["o", "ko", "mo", "go", "to"]
    bitsunitebps = ['bps', 'kbps', 'mbps', 'gbps', 'tbps']
    bits = 0.0
    bits_unite = ""

    def convert_bit_to_go(self, bitt, power, unite='auto', bps=False):
        if bps == False:
            liste_reference = self.bitsunite
        else:
            liste_reference = self.bitsunitebps
        if unite == 'auto':
            unit = liste_reference[4]
        else:
            unit = unite
        bitsdivisore = 0
        self.bits = bitt
        if bitt >= int(power):
            if unite == 'o' or unite == 'bps':
                return [bitt, liste_reference[0]]
            if unite != 'auto':
                while True:
                    bitt /= int(power)
                    bitsdivisore += 1
                    if str(unit) == str(liste_reference[bitsdivisore]):
                        return [bitt, unit]
            else:
                while bitt >= int(power):
                    bitt /= int(power)
                    bitsdivisore += 1

            self.bits = bitt
            self.bits_unite = liste_reference[bitsdivisore]
            ls = [bitt, self.bits_unite]
        else:
            if unite == 'auto':

                un = liste_reference[0]
            else:
                pos = liste_reference.index(unite)
                i = 0
                while i < pos:
                    bitt /= power
                    i += 1
                un = liste_reference[pos]
            ls = [bitt, un]
        return ls
