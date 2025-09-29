#Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.In other words, one of the first strings permutations is the substring of the second string.

#the idea is to creat a sliding window of len(s1) and move it towards the end of s2 and see at each time if we have the permutation or not
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d_s1 = Counter(s1)
        i = 0#pointer to end of window in s2
        count = len(s1)# the number of chars that need to be supported until the end of the sliding window
        start=0#start of the window in s2
        while (i < len(s2)):
            if(i-start==len(s1)-1):# len of sliding window is exactly s1
                    d_s1[s2[i]] -= 1
                    if (d_s1[s2[i]] >= 0):
                        count -= 1
                        if (count == 0):
                            return True
                    d_s1[s2[start]] += 1#shift the start one char to forward
                    if (d_s1[s2[start]] > 0):
                        count += 1
                    start += 1
                    i+=1
            else:#len of sliding window is less than len(s1). Try to increase the len
                if(s2[i] not in d_s1):#if the current char does not exist in s1, then start a new window
                    j=start
                    i+=1
                    while(j<i):#shift the start to the end of current window
                        if(s2[j] in d_s1):
                            d_s1[s2[j]]+=1
                            if(d_s1[s2[j]]>0):
                                count+=1
                        j+=1
                    start=j
                else:#only increase the end of the window
                    d_s1[s2[i]] -= 1
                    if(d_s1[s2[i]]>=0):
                        count-=1
                    i+=1
        return False

s1="adc"
s2="dcda"

s1="ab"
s2="eidboaoo"

s1="hello"
s2="ooolleoooleh"


#s1="kuzntqeuvaszrspkgjvxrupwxwrexztptsowceibeewxbslvosbobmyymikdscshybtmanuxeqtanrjekbwirmhgvfmzipfiqxcilarfyasoayepgfzmdytlpjymeaztsyubkbmblepwozffxiitdhwaquozlfmnascomqczrbhxcnzugppddtudxrigfeaozzojpeamnobapgwksudbiwdedvprwonmzardsodhxmkgghqzfhorjaijdvwzsnfpdfklwibbsnwqsoajcpjisbgizgttlnmclawbgnhbmtcpuusuammvgxnopdngclxumgfgwjrinamevhirpmlkwtyxkrmoffrreotdosjghsrkgxyiyrytbbofgczndgmdalyvvoljczcztxitxelywqemjigtuanubpstndwzvtiejtoqvetaehvcuujyupncumjnkesmoadzyvkwvjqgqewvvvpheyyvkewefbjjqzajxnhouodanyruqpzdcjmgnxkmhsgqjhpcyviewmrkfioudzqivmmguxjxuxdmpsmkwnvbxcomifgxqmcovlkooptjpfxjllwtlkkoaayzduodgsusaogswmoqkznynwiukkrrxzkwcknwlazxnlmghybxmyvquzbdqlpfydhnnuvlmyjmixyzso"
#s2="zthosfejqodcstlqczkndmgwtcakxzxaklkrehkfwnokclametzpnblcwaspdblfoopsiqrpzlbmlysddlqxcjzezcpknwzljvhmqxqinmptcppipifchxexlytleambzwmqwgvxlehnecdqsqbrxqfwvcovgdvtmwbnvajvkizixbmuiuyuixjhiohimghdbohetogrhzsbzgpekosxcjglsrvzenovpjyzknuumpsdrufcjsyfbuwfmaaztxjbpjctnuwcqknnemptjbgfthyafeatskfmysaioqikcpywmefujnvthumyhareltknxyvqprexgbwyzodfkinltwobeukrmpyjkrgvwhbtnzaozgxouxndmkyvzlujhxxwebptykctbojgnvcwhhgsyohccrqxksdyygcwdsazlznhqjdddisjmfqvjqcquuvjrzkcvzpxpfakbkrqlzacanqbggavezedqmoffxmkrlcwxdeosvhvvknqimwpasrlldewvhppzixgcxisysgeppcwfknecupyrrqnkhvessintrequaqiuoesgyndovaqxnlldmdupjcjzejannfjfasguyvgsdakwxezrginhdstbrtqmznpkasytqtbfyftwhgnuazcwehsvcdukuifmkefzabxyhihgnldpsvglubalbsvqstfxehvnpxmrejnkqacafuvzghbttgqmjhqzejasoasbpjirfawcvwahykvrfpaadcgvxssebdznzyvamyilahahgdslwvpuvzsinbbqecdqyvwnucjzyxmxwqwyxbxoljnjcqqdumghmcvqpcpjlxemupospxvkicqvyiavatbojgzurfzitgpeqjmvsgzzqphciyweyavebslgegjcyqmgehchryyclswjequeijzpsvuercqzhwgtgyxhxavhqkrwqdvkqvklicxpasnsnbgybtufdgbwrpaewzwczabckvddtewunsktcznqkivsubdjrpzxtsohiilcybrwqtlfqmjzmvpbfjmbjvbpwietkyzwzizwuiohjuhoekejhmkrooeyydmavdencmxhsxdnyitzivlymzyqogdhzrwhbdupborzqihurziajjwbrfwkzgbpmfgtobkbzyijcgkszyuyouyxvztmmtaqetcaxqrkbrmkzyokglckifgdfidjqoiqrfrpftagxxoqodbyygdioxdznycssxjvpotsrptttrbjayhugecptuibezsyggqcyvzosvmlpwmnuhovvhfyazkdrfxlxjxpbkkbuexxnklhnkteyjshhlojnbxtyltdfzhulcsptinpsskaeowofruejqpinhivlpvvosppxtbbrebvfihmamdlvsjirwfzhzmaqzuryakjlzroxrlwccdannvzwenabvosplnwhotxyzxhocdnvsekmnepzzqjhqrokocqewpihhyftshsfehijlvpajrcrgeqqjigmzkrhcgafqkdkrkkyausijdfzqewawxurtzhioqqnoxhbrdrriveapdebbwbrnmpcakomfhpfrqvzmpqkqucoepjklaqtirgkcrgpdhvyxybnulrchqgbupjdxxalbwljfpdjfnlqfquhdxvvuaecgzgfhulhkkvpuexpssodxqxhrbpzzgdiohxzjxnuhtavlittooxkuededfxdaabuzdlwjhitwykqdvtrwuohpvpgpeudhpslpvxmotibojtgvohqaaowiofdtgbkiiurhcfavlgsnqxndcxyxozklduxqeovzrtwuhoikgpyqoqwllagzufkuzntqeuvaszrspkgjvxrupwxwrexztptsowceibeewxbslvosbobmyymikdscshybtmanuxeqtanrjekbwirmhgvfmzipfiqxcilarfyfsoayepgfzmdytlpjymeaztsyubkbmblepwozffxiitdhwaquozlfmnascomqczrbhxcnzugppddtudxrigfeaozzojpeamnobapgwksudbmwdedvprwonmzardsodhxmkgghqzfhorjaijdvwzsnfpdfklwibbsnwqsoajcpjisbgizgttlnmclawbgnhbmtcpuusuamivgxnopdngclxumgfgwjrinamevhirpmlkwtyxkrmoafrreotdosjghsrkgxyiyrytbbofgczndgmdalyvvoljczcztxitxelywqemjigtuanubpstndwzvtiejtoqvetaehvcuujyupncumjnkesmoadzyvkwvjqgqewvvvpheyyvkewefbjjqzajxnhouodanyruqpzdcjmgnxkmhsgqjhpcyviewmrkfioudzqivmmguxjxuxdmpsmkwnvbxcomifgxqmcovlkooptjpfxjllwtlkkoaayzduodgsusaogswmoqkznynyiukkrrxzkwcknwlazxnlmghybxmyvquzbdqlpfydhnnuvlmyjmixwzsoufvjlrqtzxvybzhurdqdtnkciiradptqxzgrkqgfbnsmptyyggwpenatlrtpvmdpveivmenzwjlwdhlhmmpvbglhxcinvhhcphgklicwwnwqbkbndiuqowwgzdczwvlazndbboublzrltxahxenivmkbwofrnkkvjixfbbctshvqzmgwqrmheupodlrnebsidrbxxjfeoqgcoscymzskvbamtxtpumbdmedjghxazwamkqdrxsqytqxkrrqcnwrtkuaocuwmyucctdnaqfjlosovveoxjyypqrbkflxrrxlnjxhkrrvjettqfzzbwbzowsufxmppazhwiwcvimmlixdzgpmfayrblbkulfopwarxlsbfkuqvhyufwdswfpxqwhuvepyslbliapotofrxhufoopqhqjcjdtleeoedsacpeqfewxehghwvfvqmlzvzudkqxinsfekpbaggbpohbtbhcvdzvuormpzadkhhqqyspfkijjcelofwgkgimjxrkwqwhpqfihyhmwdkwhathcxvxtuopufsjaagbamghtsjewrpooxrprtvqpslsbaijrzojgwhekijtfugwbvgdltgpentcyjbwqjcdqkhicbsdvgtvsecpsacesztkjdskoumcheqzmoijoimnmnhfavttfamkkvugpmnibdzhcieyhhctifhbvqrllslpvymjamfmgladmpeqdrtumbqwcwwkduavjokhjrdbdozxaqemvurjwdukuwrbzfstuesjqfgblvvaqemylqgrtfzdrfgtcbvaokygyidfsbppasppzcunjwbrhqscumnrugeyxqvceninwsvmqcekvuetloevkrntgsrivpebgoobcggmgwkrzagkdavpejdgkpokcdpvncsmduzhowhdjklqwyphevtaugcabxovxgjovvgzksukpnadsblbpnuuihxdkovwsmniptwhrjxhyitozdwgkdkasspklxbyfmmugmawjflmrdiqmolsufpyzkrrqrvgnbtcogomdjrymxgnocnmpsdmbncterfrrxqyrsdqjzrodttnjbblleexyvfzxemlxfmxbzffflpyifrqhbdnwpuuwfhskfevjshsxvhvbldqyxenpxkvamashnbmrfiladqnuzwltrkoegwxrjveajpyvchyotakniwcyigejnaspdfjssacnfhbyobgrovavxoclvkgvgivoiycquftjuqynabeqakugedwlogqfbbivbzisljreuowaxfaugjunbyrcxvlqjvvuewgprwfiofxyzdaomzjfystxrbpmgdwyznnuzibozcjtsxxastlhmjpogvuhdtfhnmrhdxihhrtxqocmsmysxuudsdquadshqncpbejkjarbhkwkstpcqgwuarnmvtfjvdzeeklwnnjdewmwdyzdfnryaqoiysysfvlxetggjhywxwvkvvuccklxptokzvrrhodicekjrffbdjxoftxbstcbxjcksqcvcwkisywdzepzgznaorlllmahrqepouqnrtbhgxnsnyhkacxhjzgvxhlukbvspfzqgguqkngncotvgvuygijtkucvqcsjjolodnbfeznuikkaghyyqtxmtdjchrgybirzkbysbgnwwqaxjsnneazxnmdyzooizcyqtxlmqvujoqhjqlnuvojlkcdybfryidsunirmymtvltnjiggwxeqowcnbukotbngjaidyvhmobdxlklwqxshkaphxwdxzonqddvstwrrtatklpujldtgrofxyunlmlwquruzekmdymzhpuuuaiyinmaedxxhhayzybsepcohcrymkysdaeagmhodvkoissnegjecmtnbydbakamurdqwwgqqfbefltdkdvyldjxynweicudbwirebvzknodfkycidoqaalxorwlvnosvcpudvsiljwlmfqpvwtbjeyydexvfmkiilwlxcpnogyeyspjaumcbrgxkeeezgyrbmtkotoyjnedraupxevwjcluyxdctfazusyqeklxpotczvkphllcgfrykpuwscfknqhfkxdihdkymiqizppipnbflfhduzjgvoehhvtqolybcshofasguaaeaakcsxqsqxpuydzhndleoxgmkrtlivudapfhefocneliicmrtishcmxmcdskyedbqppswqnesziwankobhaxklswulygdojhpobyezjzyengtfulymybqiodmkirqpggycyouzqhrexnntvnlhhokdyzvudgilvqpjkeactaivsjdwfesruusewlpscumpqslulwrhramanthuogjdadmqjeccbutdfexdcsbqujpqdlryelnzvfbncrajicdnomidvmspjljjzglnahdmrctedjzdtozllmmyeamctrcyrzzdzwvfqgjfstbtitgmeogjpgllpihylxgupxxqmheusrglbampwrhtejoqqjkcljmppmemguapopatjkbzomwegkrwxblxgymfmurhfokjkhljtxosxtgmaldrjjhxrcvuddvzlamavxpzszsrfepfsukadtnwyzhwdergrofmetngzuifiuonziduvucichmxhmxrulpykwedymiycbhcsvrkctvqqfvygtlyhlqbrwvmbgnwlryeotjkvowxmdlyjhyvtvyognldmsxqlotfzvxrmdultwbsnstmjakjaqqpfurvwturqyzcnfkoxumuquwgpersslowdvrnssqcgwmfnssvtobdwcscoikoythwhsxswsmsimntribaohzrmjculdnnguchmqgyzqeipuumwgizlvjmpvyotgzmtsantswdarbyaklpiclafgqdaoeiitxlcpwhlqsidkb"

#s1="ab"
#s2="eidbaooo"

#s1="abc"
#s2="dabc"

s=Solution()
print (s.checkInclusion(s1,s2))