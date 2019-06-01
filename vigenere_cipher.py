from collections import Counter
array = ['gvijyzpclgfnclpkpreemkcfxevwdsaafgobeawwerehfgobeawwhrusmpsyglzwsxqiryacoowltfvhiueznirysfoefgobuhidvvuavwskccowdkqtlwbikmaatyjavvbrekfgobusgaeeeeqstyuhmktftyefdvxevqtyknkwljgoxzeiuhidvvuhenekyopsyvtssxprrevtatmsgaeeeejackkoroikjtlwbrekpsyvtojtofmstjogrehmpfpopvtzusywbfzewgrcgnklhjqfagouuoxzakaoyuaeueilhvdagclraevgfsqookasqvilhvdoscszpfvgnkcnhatjvipdijptifolihfgobuavwomgrjdonknkgnkqtlwtrdlikaeftlwsfhawsnuoaoanxnixllvjeehslpdijtygwmfdfysxzijksxzeckvmfgiqoqgfkjelgujgoguugkehtykjeieiegnxhrfhewkoioigzavnvijrvuezsnjcnhzijyijwmiupiluekainaeuvijrvuarvtygivsdfrtivsfphejrplaqwsgqtxwrvxarkvvtriktygriasrnexleinymfgfptlwlzxiryrfqmxsbcgarvaewnwladrehwnmglshefhyidlfyiwzprtcleeevahvrvusivtforlhokvevanvoevsluiriwnzpkxzegtojwsjqrefdyksaafvcrikpvckmfgjjavhlpctiscyqtlwrswtxzepcrifokuhsmtzpgxzegtojwsjqrggnjkdijsjjoylieitstelpcmnicksivyfwribobknkeitjaidsrkdxgpvvuraayksxgnvknhacrvehlhrvhioajxevqmlehexrrkdxzakuhioajuevaolumckijvevoajcwmlcyrexmnzcrihervehkhvnosceuhrmyhkgnivblvsxgoujevyrfwnhzeijuwtaefwekankzejdkjiwasrdsyjddkclsecuamvsycrtdykjecoeigaxguiyehvieitlwymksmleuhovuhiksxeajktsddkjeqqolyevwnkvoofonrexmnzcwlasggrivblvixktiwemnejgerlhzpgwlhvrrsxejuovjocnehzijgyikdvcrmmnugrwlaeftlstpquvwnfvfeeickavoikjtlwstgpxacrnlmleictyjepquqsyeqtvwacksizongawqikksjgrrvreanvfmeyitkarlowckilhvueieieilcamgqswabcgrieeddevzonktemgyvhejrpvofwnuupsgnjkfmlsvgmivlzmexzepeoyddrnweqsxwewkwyctcgungrilhzpkmfgkjaxkcrnlivcfndvwauknkatncsrlbvpdmfgjrosfsnjaxoajktxzeerexmnzcbmlhvtlmhitcnxbujvtidlpqucgucntlanbkmwzejyapdongdpaskgnqacycepawrunxslncywdibgtlasjjekwskwrivakjevkechawlhfwgllozpdmuakghijlzvhixoiolmdyukdxzijdegsujgifwcrwsiabvigivhvtfsjyvcrwabvigivhvtlmdyycdedwrasfweerriltzgrxzaeoeefdzfbiwndgarloygrfwcrwsigfkjaxsnuvhifsyggslmriiguaeaoyamriirwhfyijwlkcnhabvigivhvttsmsvuoqwowvhelmriiggndgsslhrviggucfbihrvvtclofgvifiwkcsmluptlsvvjeveaxkcellvcsxacfwlhtegtexlykgavkwvtekstygrmfgzppiluekawwyvuarvlznyagucftidldgnssnuoaowugvhieojvrmvitwlsmsvzcykejniowtygwsjluyoyddvpdmxsygwijeekciloygrwaskgrsjatgnxsuivopvhvtnsltfvhieojvrmvitwlsmskjirysrpdmzakgdlwrwqrmlaefwlwnzjahbujvgvsdlctivfiqmyfimgrwatpkwekgfknkgukyixztyksfgymgrrgnuwrwdepjeasswctefdygwektygordysqyazonqupvtrnkxgmvcnhzejcihzencnxwdtjipvrvparvtyctlaswkrwlsfpwsmludersmvfdyvlvaarvikjoyyhkvoqqsvnfazakmirvowravwnkpaqwskjemjcyklhvuunecvuiuliqikyawdibgiwswdawlglvhuxmrvnijwsktexuhzpgsmtzpfvgnkqfqwaefiggucfnxktrpdmlaefiajokgtseyjksxwrrpdxglujevlhrvijkhvfihftyglteezfrelhvtjyktggtyfirutshpvfarqwrapiluekawsiujevnozeeweacnslwgrxemfsygtsdddgixoajfaryeiquwsnukseadzfihfttcrisnpoovwaefihjaemtlasgqtmgnrpdmoajuigcfftwiwkjduxohvpikgtsgtxwrdasoantneejeuwpefdzhirslcafmdlvfoylaefiasssgayliwwltwogneawrvpigwtfoelwrmqigwbiqkisnucfxwrkjaxacfwlhftyctieyjksxwrrpyqgrvgstwczclpqwygnmdertnivwyctlwrdcgmubiqukztygrmftygervdrtlmfgdkclsecuamvgvptpqyfwgslszekcguxcirwdjqmioezihxohznevwskknkansgdefdpquvkkzpcpwaigdyhoektwgweqrfwieismukdcdiqolehefgvaoyjdzgtwzencseoikehtwtlpiejeggaxwdzuaaatggtyfiroigzavnseadkjeefnfaaruencsgjevriryievolasmqigwyfwkrgwkjaxuaevbilrlgdsarvclpqhrxexgeorleannjytwtlpieorlpglwrycnhksygsiwmvftstefptlwvvtgigfkgavkmpnozwibpoaacrptaanrtgyeeevsaatyaoytukrlissvaoyzamgtslrlutqwoevhmkdrfmyetygtagowvhieskqptwdrpdpgobgdelhrtrcsskjoyyhkjecvfftgsltvptlwrvyawstykrhheiuorankjevgodjavjykqoosdvgpfjervhqmmpquvhaignxkdzfnxzamgmeyitfihlhvanshekwnmssrkdpgobknkhuqblivtygnrgoegirqoltfeeicakrwwrdoylmriigohvplmdyxqtlwrcgtxwryqwhadkjecyekeornieeehshggtyfiruamvtygyhadevjyktjgnhslvvtijtygywwnkcpvgfvussjfiqmlggncrxkhvrexmnzcsiqejhlmukvftseitjaidhvuhsoeuwswgmvoakackjerqolforlhrxexgfzihxgvvttlasycrvqsrkdjardnylgpzpgeyazpsxzoggtlstkjiwlidgjyktkjiwgntgtlwynqupvlzutiftfjiqafzvsxjuvyegsnawsxyekchsywrttwhrfhewkoijevwaefsiwtygmeyithovguiuepnejcnhvauyipdauoixlhrvixktiweefdzhnsltygnqmmnklpsddktxzakktwxacuexzakuwlstkjeippvtiqwnkclqwtyqdmkfftsslhrvwivoevhenekqrikocxexzieisnmskdyejglknklhvrrsxejuovluipehsnunosceufoafakjiqvijoiwkimgawmslclszcfoergwycrvqrvclpqmriigatyqukztpquhcnfybiltvttlsnkqtecekjiwkeikoyklpuorwvvpijqoltesflpvereaxkcmkjlutetolvtlwmfutyfstkerliwkcxzieitlwrvkslsriasqgukjtaaskgdfatkgrpqhvyawlrvctivwvnltjoscbpqbvvtijtycnqgskierwtzefelhvtsxjervehlhvkrsontjipvrvphejrpjahtevpsiftkqtlwbvuttjidcrckcyqopkaefwlwnkjaxviuptagrbquxzencstjomkdivwzvhxmtftsjjodvhiwnunewkpfqlsxskcrzanxutyveevsedwraslsriahevbvgnifcfwreyeuvowluuawlstvxevualihxzijctxwnkkortolihxslcvhitofmsxzakeayyhkjiwxaeeywhoeuovwdzpwlstvxeveakjssjstkeruetqmtwtzvisfsygerleigdlwwrugmneecnclhzpgvwajqnetlvvhelhvyarleugxgwpkoactekjewdixjtiktjjrivowtewhetvahgckqrxwatjirybzqclwmzutvqakqxjgrueoyddycrhdysgebhetvehlocksxwnkqtlwauxigwowclmltcgbsqyfwwsmluniwleevowzonknxwrvutsxcfwrwwtyctwohrvakgouravwnkyoydduqarvsfkfcgutqngwimgdsxyfwrwwlwcseyoffpejeevysmwfwlhvozvbyltrmeeleeaeejocfsijifwspqhrtdpqsfoexamvuhejrpyarleuvowurvcmelhzufelhvtmyehrtrckazfijqolyarltfyirlhzuavyudgnxoikjdevlfqkmfcycpxwrkyosxtygfmjskdoscowvhixeppmeflvetyjejqntzyjkcwlhvtewsqlqtilhvteetolvhsopyklskogjevksraakjervdislrdoylwyctwuivpcisbjqlylecariiuztewsnuktmkacnwvgnxdegsujgtlwoenyvmlvknwuivpciaskjaxlhvhirslrtbmleiksstsvtvelifptlstpqunmskjazwtfnoscakvhiooindefdigpsjtnjaxqolueimmfhfxzekqpsxmpjeevitcnxlhzpksxwygrilowknhkodgtlanxcbsmtyqwmlsrpihwacqfwuivpcilojgtxdekjiryssaebheikmiftzpsxwauqfejgloerlsyksqgtygrpgobgdhgwectlamrpdweicgdxzaemysmhrtrctukjevzerfrskesccompkqsxsrvctlwrywsfsnukdsftncnxlonknefaiiuqwnkyixzyfwrjstygrmoaevmczujdarvtfvopaskgnxghzuwmxenjopgvvuhmeaeftvmskjevbujvtlasfpcizaitygdojgdlasvaewtrzgfpqhfrepwsjdoxzowjiwhaignxkwvtenmskjotwlvusrgwykstsrvptwoeiggiltzpgmftfqnigfkjowwaiiuqwnkuaksieqniohvtelasdqtlwrktiivtfoaowhzufelhvtfiwlxwiplyrpdlaswctlwrktiivtfoaowhzumslhvtfiwljvutadzogsanxvokgtfoyvgodjavjyrpnsmntgdlasmqigwtigmfdeuclmltcgppwajgtvqnfvtsxixjtxgodwclsbfwtxzijouqvauyepdkeqwwgoegnsmgyjoaattqmikolvrmyhkqfgguiuelsriaseadyksjstygrefdyksqgtygrksvvjiqsrvcswmrzpgoasjcnhlhvptlwyngnxgnwkgllieiwlalvjavjytniqteuvhiktrkrwloyksfwdiqoqzejjuxlhvfosjbvjirvhzoarvtikehlokjirctygfyfnpvhmfgncslwsyqupvhrxeeyrvgdaatyfahfofpelsdvxevkevparqemkdifcvqfqsgzearvateovvieitseudvhijencseohfneqsgzeapooindsmtkjevwhfycsmlucncgnvmeihsfoexzieilmcekjaxssverilmfteqsgzetlstjgeqwdckkisrrvhijslupmuifwswgrkqfipcluemlsyqupvhrxefweeccpwaeeawwfftmyejfmirylpknkgrsgiryieuarwiecsgwnuknkgrugrsxanhupfejuijeudjahkeevtlwlvvtijhvtsidfkjaxoolndippccirzonktejrzxehstkjepwtkgrfgxnktlgukcsxsmgclmltcgirkaektcoajhavxainewkidrrstasnexzaevhimnzxevkeigapdynqroanxniowtyctipcvrtxzakuoqwprttsxhrtrcoajwtxwrcacsfvzpcivtyctqsgzewekrvclefdycdfweeuiruekjemfskcnxzejcwxzegwtelimgliltvtfvgmkjelggncrxkstjosdowyixuhttajlaefwmraifrczaityvmbsgdlaswqrizerfgvamreirydfptfwlzgviwvvtyxzieiysmtyknognvqflassqookhrfseadswtxzijdidsrigcijtrknxqhrtrcoajhirvieihmesvnfnmskgxtwckknklhrvyikayqgasrkupvgfvussjwfwlhkhfyutsnuyazwancnhsnuoakacnqupvcfoesmtkjewlrrpgiueivamftpyaweabknkfovhfsjtkqgysruktwwlwcgeanjvfedszhigstzqnassevmecieiebuujgsmfauxaruewqrazykjevwwfwlhftsgatjowgswgrfttlwpiqfiksftwsmluqnpqbvcbpwtfdervsgqorkwygrivopquggmvhrsesktaryecktxdegtehackkorzaityharvetivtygtlguxjtelhzubvsieyhcvozdepaemgwlstzdepaemguwmacnylsriawekpigtxqgfqdelaeuwijieitlsthwewlifpbylievhmkprttmuuccrgssvjelsdeqcpmenjaxzijdreanncsxziemiryhrtrceeevapdyjjryygvfajdakoexslgnaxwoecdsgrrhfsjdjruwzieiarvaycnhdefpahgoicfjgruupydlzpgefdkjexzieitsvonktlstvutetlvjytgtygsmkijvokgaeftiktzvhilofmataetgojdiegdtspvtfvgmykshwsbcnhktrttivwiktmfgugavvegwtczerfmmktigswzaitytsujgdvwfcgcxanxvhifdzucejdvftlwprrevxoicnslhvttehpzpgefokjeveicniqwtigojyrrrhmlewtoqzijoegzaekcedpvpcmdtyksgslcgdjgrtcrixuceapdixtatzyugavvegwtczerfmmktigsweiegrzsmtiorsgrnlsjwyqmwgemgrmlmracsfcvtnmjetgnxdyigciavvfysmrcgtxwrfhaguegvaruekqhsywrttwsdutewkeuvoqjhgqtxwrpquqsyeqtfwancrilhrvmcyeegtmuprterlsacmikpfvtijaeflmdygqtxwrwqrqwrcalmdyvxarkaigdisdzyawsdfrtivbpnipqsjksxwrggtyfirgvefsmgrvwsrpdlwrywsfsnuoigzavnvijrvuezsnjkaqwxkteqwlpknxwrvutiviectxwnuknkzoxyavlstqnhatzqnedoeuugzagnagwatvuedlpgxmktzpgsflpoyqgtygrtwtlpiekapuslwkeqwwsbfwtqsgzearvsygceftluemlhvtsidfdafelhvtiwzixjlckcvrtmuackmckechaqmntgrxsiekapkouqnxcnfywlwrvvosttrknefyfhtlwbfqkwgrvsumhmvptpaskgdmfyfwreucvrtefcvnexleiooxzeioerlifpehlhrvysmsvptezoxyavlsigpvwsvptelimgtsdicapsltvttlwncklcwvrpsmfoifevlougmsfsktaxwtfjevxadklclhrvmeyityawjernarvigtewmmvjephlznysttrknlwrjehsgldctijirnsmxyfwcsmlufoxzijhoveyfynjsmznymlwfwlhtevztvwmvnylwlghupkieeevwlpjavjyacmikpfvtijemcnwneitewzaityevdvftlwiieuvjeevahvrvusxzeehopveuwpxzecgtxwrrpdtmtzvirsnvpvidoggwlacyjeevdigswwdkqhsywrttwxuivhijcfpsmveictmgncgdlamkqoflazpagsnuneefdutitoaoqnxgtygfpspfhtlweexepgpvknxgwykclmszpgeheemnmxejvitzezopvwsjgdxzezpixaacuhnhemkflwwrugsanxvohwstgnhankqtlasdcdrwsjjeassxqirytffomlwzvhwlycgtlwnygotwnvfhmkdfqrefdngnxtatmdsonjvamjsyksjstygrassjktxanxknxzeckvmfgiqoqsnuteevieiafgobqflagygrqstyutskhfyhsosdcrxzencsefdyksqgtygrasszptlwkzvclwngtetsrzpgsfefhhmkfrvhijswcvsmrzveqwacutskhfyhsolfxirysygwekikfihftcqoodibgtlwyngrilacmirytfqnisnfvhijakclpssjeavqajcrkmmvptwuolndfwnfvavyuzpgassjqmizonougzwftsieudjavjyjcihankqtlwuepevnieismdeeeemegfknklokgsxlhvjytgtygsmkateovvieitsqolttlwoiahsodfksifdrpoadtfjokoaivslasdqtlwrkwrrwdwtoqlhvmixuhvpsmfkkqsxsrvctlamcqooanxuhsukvfimvoevkrgwzvhmfkpqunmskjazwtfqwrsmriiggwcvhelsyqupvvvuoyfdvfhmyhcasykpzeismsfjsslhvtewfoncyxgtvutcguivhigrpvhifblvtlwpveupaaieevlazptcanycrvqsvgmivwznlmfgkqsxacbktwfetmoylemgnjmrkjevoecntlwlvvtijgfvhijejqmizonjavjyjcihkoznlnmskyazwikcrsmnuquxkiugarvcrnlpwtkgrjgryqgasrkuarvsvgijsnfyltacbuixmpucdhgyfwweftkqcseerpdasttjhmkfrvhijsyqoozijjeevmzpuxwlpcnhcegvorjerfiryoweoyjsvjavjykjoyyhkvolamjgljeaxkcassrfiwyrreejmlkjirytyctsflputyhiureshlvdepaemgdmfiwjiwxakjevoeevssxaicsxgtvutxzeyapslhvuiwgrvxeroakehmlbvknklejvehlhrvwsmluheidlzmeeksfeielieihmesvnfaatyvheloenyekhrtrcktlopivolvtlwbrekhgoiknxgtygbeukxcrhwnukdmloteuvloykmxzakkfefonndmvcfoehgwecnhknrvcllhvnexleijeassxqirytfjazwsfoexjoldlilecnirydrfafgukktfmtnglplhrvceftigapdyycptwntcnmlnfoaxleiyhelmpdreanjgeqktfdepaemgijsnfylvwacnyggmvudsonrpdkjasutlasvpvidoggiqyozpgxghrxeagrikewslfvmsjezopsjtrptxzaeyheldrftlanbuhejrpvoscaugettrvctlsnutamkeuvhiwnmglshezptslhvcivzejyapdongdgslcknkguknexleihovzoxyavlsnjipwhfndmfgrpernecqpizixjirlhvcivankjeqadunesxyfwrsonsccoyaiferoajccxmacnytjekvyiebrtrekszpgrgwkjaxzekjoyyhkcbsmtzvnsamsgtxwrkjarvaukwmdlluexzejeiiftzhigeekjohwvvpijatdckikmvheidskwpmvlvvtijhrtrckazfbylikccxmacnygsmvquxssdqrigfryhmkpvtehurfcklsriasxwecgdlasnklpsnuuhsmtvfirlokjeiepkasoqlvvtijffthsywrttwuaekgilaeqwpzaityekkvfafwmluehoodcnwnozeesfefhtlwnvkgltoltslsriapydlvfdsonykslsnuniowikyawgnwkrisnujihlhvgnzwlfrefwhzpdlassccodibgixoajfryymfpeczijyhsdewccioajjoxoikjslsmvcnsddnqmefswccihevtehgukhrseasqvilhvpemyhsquvanxheruextidrlvfgvwyycivwstcpmfgwtoqzeijamjnvvmvkfzigxzefecekifpaptasasmltvtwlstrtecguuqiryhrtrcfokjiryhrtrckazfirssktarylvfvsacvluwltvutmfgrteedlpuipdykjesjyukdcguxgtcguiccgwpkcngwlvvtijfiqmlggncrxkhrtrcxrfbemfpccciqejjavjyjnitksrkdedikvliohznepstvtikgtrnexleihrsehfiwejtjvhiqsratlwyncnxeyfylfqtygtlarkafmjskqfnmlpduxtukaoyvoevhenerpoadpfqrhwaikceftzoakanvyhelsfoesfedwsxzamgbiwnkjircieisifdzpgcguawsxlhvutefdrtdpwtkgreorzpkpwdrtmwlrvvclwdfwtsneivhixeeeeefdfrerwdrpebhetvarlhrpdlsrunyineevhmfkzpgeltykstgievhejrpiazwomgrlasvpvidoggjyktcgazwikvoqwdvcrwsiuorwxixiarviecjmxfpqrxooznllsvvuoqwoegozwrrpdlwrwccivijcptwaigdjjodqvijtygfifcvvhijencsedoeismdeeeemftyggejdvptlwnrdockvfkcikazfcedmcaarvqlkexdynjax']
ciphertxt = []

for i in range(0,len(array[0])):
    ciphertxt.append(array[0][i])

letter_num = {}

for i in range(97,123):
    letter_num[(i-97)] = chr(i)

conv_let = []
for i in range(0,len(array[0])):
    conv_let.append(int(ord(array[0][i]))-97)

def substr(key):
    no_substr = []
    for i in range(0, key):
        count = 0
        temp_arr = []
        while(count+i<len(conv_let)):
            temp_arr.append(conv_let[count+i])
            count += key 
        no_substr.append(temp_arr)

    return(no_substr)


#print temp_str

def error(string):
    letter_frequency = [8.12,1.49,2.71,4.32,12.02,2.3,2.03,5.92,7.31,0.1, 0.69, 3.98, 2.61, 6.95,7.68,1.82,0.11, 6.02,6.28,9.10,2.88,1.11,2.09,0.17,2.11,0.07]
    # print(len(letter_frequency))   

    # inner_temp_string = ""
    
    beststring = ""
    bestshift = 0
    besterror = 10000000

    for i in range(0,26):
        inner_temp_string = []
        for j in string:
            inner_temp_string = inner_temp_string + [str((int(j)+ i)%26)]
        #print("!!!!!!!!!!!", len(string), len(inner_temp_string))
        freq= [int(0)]*26
        #print("kkkkkk",inner_temp_string)
        for char in inner_temp_string:
            freq[int(char)] += 1
        total  = sum(freq)
        #print(freq)
        for frequency in range(0, len(freq)):
            freq[frequency] = float(freq[frequency]*100)/total
        #find error
        
        error = 0
        frequency = 0
        for frequency in range(0, len(freq)):
            error = error + abs(letter_frequency[frequency] - freq[frequency])
        if error < besterror:
            besterror = error
            bestshift = i
    return (26 - bestshift)
    



def regroup(temporary_string,frequncy_string, keylen):
    plaintxt_temp = []
    cnt = 0
    
    for i in range(0, len(to_shift)):
        temp = ""
        for j in temporary_string[i]: 
                       
            jmp = (int(j) - int(frequncy_string[i])) % 26
            # print j , chr(jmp+97)
            

            #plaintxt_temp.append(chr(jmp+97))
            temp += chr(jmp+97)

        plaintxt_temp.append(temp)

    final_arr = [None] * len(conv_let)
    for i in range (0, len(plaintxt_temp)):
        for j in range(0, len(plaintxt_temp[i])):
            try:
                final_arr[keylen*(j)+i] = plaintxt_temp[i][j]
            except:
                pass
    final_answer = ""
    for i in final_arr:
        final_answer += i    
    return final_answer


for j in range(1,7):   
    temp_str = substr(j) 
    to_shift = []
    for i in temp_str:
        to_shift.append(error(i))

    
    print j
    print regroup(temp_str, to_shift,j)



#fre_anal returns an array with key numberr of elements
#each number is the most frequently occuring letter in that substring
#assuming that the most frequent letter is e


def freq_anal(array):

    temp_arr = []
    
    for i in array:
        count = [0]* 256

        max = -1
        c = ''
        #each sub-array is our list
        for j in i:
            count[j] +=1
        for j in i :
            if max<count[j]:
                max = count[j]
                c = j
        temp_arr.append(c)

    return temp_arr
         
        

# print frequent




    
