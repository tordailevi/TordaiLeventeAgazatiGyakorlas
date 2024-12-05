import ertekel
import sorozat
import lotto
ertekeles_bekeres, nap_bekeres, tanora_bekeres = ertekel.bekeres()
ertekel.kiiras(ertekeles_bekeres, nap_bekeres, tanora_bekeres)

szam_lista = sorozat.randomszamok()
tizzel_oszthato_szamlalo = sorozat.tizzel_oszthatoak_szama(szam_lista)
sorozat.konzol_ir(tizzel_oszthato_szamlalo)
sorozat.fajlba_ir(tizzel_oszthato_szamlalo)
huzas_lista = lotto.file_beolvas()
lotto.sor_kiiras(huzas_lista)
lotto.huzasok_atlaga(huzas_lista)
lotto.legnagyobb_huzas(huzas_lista)
legnagyobb_szam, ev, het, huzas = lotto.legnagyobb_huzas(huzas_lista)
lotto.legnagyobb_kiiras(legnagyobb_szam, ev, het, huzas)