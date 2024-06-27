from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'contractor_hi'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #Demographics
    age = models.IntegerField(label='आपकी उम्र क्या है?', min=13, max=125)
    gender = models.StringField(
        choices=[['0', 'पुरुष'], ['1', 'महिला'], ['2', 'ट्रांसजेंडर'], ['3','नॉन-बाइनरी/लिंग गैर-अनुरूपता'], ['4','नहीं कहना पसंद करते हैं']],
        label='आपका लिंग क्या है?',
        widget=widgets.RadioSelect,
    )
    company = models.StringField(label = 'आप किस प्रिंसिपल कंपनी के लिए काम करते हैं?')
    site = models.StringField(label = 'आप किस साइट पर काम करते हैं? (यदि आप कई साइटों पर काम करते हैं, तो कृपया वह साइट दर्ज करें जिस पर आप अभी हैं)')
    employer = models.StringField(label = 'आप किस कॉन्ट्रैक्टर के लिए काम करते हैं? आपका नियोक्ता कौन है?')
    owner = models.StringField(label='क्या आप अपनी कंपनी के मालिक हैं?',
                               choices = [['0', 'नहीं'],['1','हाँ']],
    )
    position = models.StringField(
        label = 'आपकी नौकरी का पदनाम क्या है? कृपया ध्यान दें कि यदि आपके पास एक से अधिक नौकरी पदनाम हैं तो सबसे महत्वपूर्ण जिम्मेदारीवाले पद का यहाँ उल्लेख करें।'
    )
    position_detail = models.StringField(
        label = 'कृपया अपनी भूमिका का अधिक विस्तार से वर्णन करें।'
    )
    company_experience = models.IntegerField(
        label = 'आपने इस कंपनी में कुल मिलाकर कितने साल काम किया है? यदि आपने इस कंपनी के लिए एक वर्ष से कम काम किया है, तो कृपया 0 दर्ज करें।', min = 0, max = 100
    )
    industry_experience = models.IntegerField(
        label = 'आपने इस क्षेत्र में कुल मिलाकर कितने साल काम किया है? यदि आपने इस क्षेत्र में एक वर्ष से कम समय तक काम किया है, तो कृपया 0 दर्ज करें।', min = 0, max = 100
    )
    #Workplace 
    workload = models.StringField(
        choices=[['1','अक्सर मुझे व्यस्त रखने के लिए पर्याप्त नहीं होता'],['2','कभी-कभी पर्याप्त नहीं'],
                 ['3','बिल्कुल सही मात्रा'],['4','कभी-कभी बहुत ज्यादा'],['5','मेरे लिए इसे संभालना बहुत ज्यादा है']],
        label='पिछले महीने आपका कार्यभार कितना अधिक था?',
        widget=widgets.RadioSelect,
    )
    stress = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='आप कितनी बार तनावग्रस्त, बेचैनी, घबराया हुआ या चिंतित महसूस करते हैं, या रात में सो नहीं पाते क्योंकि आपका मन अशांत है?',
        widget=widgets.RadioSelect,
    )
    fixed_mindset = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='आप निम्नलिखित वाक्य से कितना सहमत हैं: आप नई चीज़ें सीख सकते हैं, लेकिन आप वास्तव में अपनी मूलभूत बुद्धिमत्ता को नहीं बदल सकते।',
        widget=widgets.RadioSelect,
    )
    company_employee_relationship = models.StringField(
        choices=[['1','बहुत असहमत'],['2','कुछ हद तक असहमत'],
                 ['3','ना तो सहमत ना ही असहमत'],['4','थोड़ा सहमत'],['5','बहुत सहमत']],
        label='आप निम्नलिखित वाक्य से कितना सहमत हैं: यदि कोई चीज़ मेरी कंपनी के लिए अच्छी है, तो वह मेरे लिए भी अच्छी है।',
        widget=widgets.RadioSelect,
    )
    teamwork = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='आप निम्नलिखित वाक्य से कितना सहमत हैं: इस कारखाने के अन्य कॉन्ट्रैक्टर और मैं एक साथ अच्छे से काम करते हैं|',
        widget=widgets.RadioSelect,
    )
    common_goals = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='आप निम्नलिखित वाक्य से कितना सहमत हैं: इस कारखाने के अन्य कॉन्ट्रैक्टर के लक्ष्य भी मेरे जैसा ही है|',
        widget=widgets.RadioSelect,
    )
    competition = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='आप निम्नलिखित वाक्यों से कितना सहमत हैं: मैं अपने श्रमिकों के लिए अन्य ठेकेदारों से बेहतर कामकाजी परिस्थिति और इंक्लूसिव प्रथा दिलाना चाहता हूं।',
        widget=widgets.RadioSelect,
    )
    #Principal Company
    relationship_incentive = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label="प्रिंसिपल कंपनी के साथ मेरी कंपनी के संबंध मेरे श्रमिकों के कार्यस्थिति और इन्क्लूसिव प्रथाओं की गुणवत्ता से बहुत प्रभावित होती है।",
        widget=widgets.RadioSelect,
    )
    principal_company_approval_incentive = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label="यदि मैं कामकाजी परिस्थितियों और इंक्लूसिव प्रथाओं पर प्रिंसिपल कंपनी की अपेक्षाओं को पूरा करता हूं, तो प्रिंसिपल कंपनी मेरी कंपनी के काम से खुश होगी।",
        widget=widgets.RadioSelect,
    )
    principal_company_disapproval_incentive = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label="यदि मैं कामकाजी परिस्थितियों और इन्क्लूसिव प्रथाओं पर प्रिंसिपल कंपनी की अपेक्षाओं को पूरा नहीं करता हूं, तो प्रिंसिपल कंपनी मेरी कंपनी के काम से नाखुश होगी।",
        widget=widgets.RadioSelect,
    )
    productivity_incentive = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label="प्रिंसिपल कंपनी मेरे कर्मचारियों की उत्पादकता को ध्यान में रखती है।",
        widget=widgets.RadioSelect,
    )
    salinece_perception = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label="प्रिंसिपल कंपनी मेरे श्रमिकों की कामकाजी परिस्थितियों की परवाह करती है।",
        widget=widgets.RadioSelect,
    )
    principal_company_trust = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='मुझे प्रिंसिपल कंपनी पर भरोसा है कि वह ऐसे निर्णय लेगी जिससे मेरी कंपनी को सकारात्मक लाभ होगा।',
        widget=widgets.RadioSelect,
    )
    interaction = models.StringField(
        choices=[['1','केवल मेरे द्वारा'],['2','अधिकतर मेरे द्वारा'],
                 ['3','मेरे और मैनेजमेंट द्वारा भी समान रूप से'],['4','अधिकतर मैनेजमेंट द्वारा'],['5','केवल मैनेजमेंट द्वारा']],
        label="क्या प्रिंसिपल कंपनी के साथ बातचीत मुख्यतः आपके द्वारा या आपकी कंपनी के मैनेजर्स द्वारा की जाती है?",
        widget=widgets.RadioSelect,
    )
    decision_power = models.StringField(
        choices=[['1','केवल मेरे द्वारा'],['2','अधिकतर मेरे द्वारा'],
                 ['3','मेरे और मैनेजमेंट द्वारा भी समान रूप से'],['4','अधिकतर मैनेजमेंट द्वारा'],['5','केवल मैनेजमेंट द्वारा']],
        label="क्या प्रिंसिपल कंपनी के साथ संबंधों के व्यावसायिक निर्णय मुख्य रूप से आपके द्वारा या आपकी कंपनी के मैनेजमेंट द्वारा लिए जाते हैं?",
        widget=widgets.RadioSelect,
    )
    #Principal Company Positive Incentives Details
    promotion = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'मेरा प्रमोशन जल्दी हो सकता है|'
    )
    bonus = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'मुझे बोनस और/या इनाम मिल सकता है।'
    )
    commendment_internal = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'मेरा मैनेजर मेरे काम की तारीफ कर सकता है।'
    )
    job_security = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'मेरी नौकरी की सुरक्षा बढ़ सकती है (मुझे नौकरी खोने की चिंता कम होगी)।'
    )
    respect = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'कार्यस्थल पर मुझे अधिक सम्मान मिल सकता है।'
    )
    contract = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = "प्रिंसिपल कंपनी द्वारा मेरी कंपनी के कॉन्ट्रैक्ट को नवीयन करने की अधिक संभावना हो सकती है।"
    )
    increased_business = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'प्रिंसिपल कंपनी द्वारा मेरी कंपनी को नई साइटों पर नियुक्त करने की अधिक संभावना हो सकती है।'
    )
    increased_payment = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'प्रिंसिपल कंपनी मेरी कंपनी को अधिक भुगतान करने को तैयार हो सकती है।'
    )
    commendment_external = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = "प्रिंसिपल कंपनी मेरी कंपनी के काम की तारीफ कर सकती है।"
    )
    peer_acknowledgment = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = "मेरी कंपनी के काम की तारीफ अन्य कॉन्ट्रैक्टर द्वारा की जा सकती है।"
    )
    other_incentives = models.StringField(
        label = "कृपया आपको या आपकी कंपनी को मिलने वाले किसी अन्य लाभ का उल्लेख करें।"
    )
    #Principal Company Negative Incentives Details
    promotion_negative = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'मेरे प्रमोशन की संभावना में देरी हो सकती है।'
    )
    bonus_negative = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'हो सकता है कि मुझे कोई बोनस या अन्य इनाम न मिले जो मुझे अन्यथा मिलता।'
    )
    job_security_negative = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'मेरी नौकरी की सुरक्षा कम हो सकती है (मुझे नौकरी खोने की अधिक चिंता होगी)।'
    )
    commendment_internal_negative = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'मेरे मैनेजर मेरे कार्य के बारे में मेरे साथ चर्चा कर सकते है।'
    )
    respect_negative = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'कार्यस्थल पर मेरा सम्मान कम हो सकता है।'
    )
    contract_negative = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = "प्रिंसिपल कंपनी द्वारा मेरी कंपनी के कॉन्ट्रैक्ट को नवीनीकृत करने की संभावना कम हो सकती है।"
    )
    increased_business_negative = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'प्रिंसिपल कंपनी द्वारा नई साइटों पर मेरी कंपनी को नियुक्त करने की संभावना कम हो सकती है।'
    )
    increased_payment_negative = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'प्रिंसिपल कंपनी मेरी कंपनी को भुगतान की जाने वाली फीस कम कर सकती है।'
    )
    commendment_external_negative = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'प्रिंसिपल कंपनी मेरी या मेरी कंपनी के कार्य के बारे में चर्चा कर सकता है।'
    )
    peer_acknowledgment_negative = models.StringField(
        choices = [['0', 'नहीं'],['1','हाँ']],
        label = 'अन्य कॉन्ट्रैक्टर द्वारा मेरी कंपनी की आलोचना की जा सकती है।'
    )
    other_incentives_negative = models.StringField(
        label = 'कृपया आपको या आपकी कंपनी को मिलने वाले किसी भी अन्य परिणाम का उल्लेख करें|'
    )    
    #Worker
    dehumanization_1 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='इस फैक्ट्री के श्रमिक  बहुत बुद्धिमान हैं।',
        widget=widgets.RadioSelect,
    )
    dehumanization_2 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='इस कारखाने के श्रमिक स्वयं नहीं सोचते हैं और उन्हें बताना पड़ता है कि उन्हें क्या करना है।',
        widget=widgets.RadioSelect,
    )
    dehumanization_3 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='इस कारखाने के श्रमिक जटिल विचारों को नहीं समझते हैं।',
        widget=widgets.RadioSelect
    )
    dehumanization_4 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='इस कारखाने के श्रमिक प्रोत्साहन से बेहतर डांट समझते हैं।',
        widget=widgets.RadioSelect
    )
    dehumanization_5 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='काम में सहज और सुरक्षित महसूस करने पर इस कारखाने के श्रमिक अधिक उत्पादक होते हैं।',
        widget=widgets.RadioSelect
    )
    dehumanization_6 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='इस कारखाने के श्रमिक तब तक कड़ी मेहनत नहीं करेंगे जब तक हम उन्हें मजबूर न करें।',
        widget=widgets.RadioSelect
    )
    dehumanization_7 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='खुश श्रमिक नाखुश श्रमिकों की तुलना में अधिक उत्पादक होते हैं।',
        widget=widgets.RadioSelect
    )
    worker_motivation = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='इस कारखाने के श्रमिक अन्य पुरस्कारों की तुलना में पैसे से अधिक प्रेरित होते हैं।',
        widget=widgets.RadioSelect
    ) 
    worker_voice_attitudes = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='श्रमिकों की प्रतिक्रिया सुनने से व्यवसाय की अच्छी समझ बनती है।',
        widget=widgets.RadioSelect
    )
    gender_leadership = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='इस कारखाने में, महिलाओं का नेतृत्व पदों (उदाहरण, पर्यवेक्षकों या मैनेजर के रूप में) में होना आम बात है।',
        widget=widgets.RadioSelect
    )
    gender_compliance = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='महिला कर्मियों को जोड़ने से हमारी जिम्मेदारी और अनुपालन आवश्यकताएं बढ़ जाती हैं।',
        widget=widgets.RadioSelect
    )
    gender_norms = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='चूंकि महिलाओं को घरेलू काम-काज करना होता है, इसलिए उन्हें कारखानों में काम नहीं करना चाहिए।',
        widget=widgets.RadioSelect
    )
    gender_productivity = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='इस कारखाने में महिला श्रमिक पुरुष श्रमिकों की तुलना में अधिक उत्पादक हैं।',
        widget=widgets.RadioSelect
    )
    geography_1 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='मुझे उन श्रमिकों को मैनेज करना आसान लगता है जो मेरे जैसे ही राज्य से आते हैं।',
        widget=widgets.RadioSelect
    )
    geography_2 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='स्थलांतर करने वाले श्रमिक स्थानीय श्रमिकों की तुलना में अधिक उत्पादक होते हैं।',
        widget=widgets.RadioSelect
    )
    caste_1 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='हमारे श्रमिकों को कोई भी कार्य पद मिल सकती है, चाहे उनकी जाति कुछ भी हो।',
        widget=widgets.RadioSelect
    )
    caste_2 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='मुझे उन श्रमिकों से बातचीत करना थोड़ा मुश्किल लगता है जो मेरी जाति से भिन्न जाति से आते हैं।',
        widget=widgets.RadioSelect
    )
    worker_empathy_1 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='मैं अक्सर अपने श्रमिकों की वित्तीय स्थिति के बारे में सोचता हूं।',
        widget=widgets.RadioSelect
    )
    worker_empathy_2 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='मुझे अपने श्रमिकों के सामने आने वाली चुनौतियों को समझना आसान लगता है।',
        widget=widgets.RadioSelect
    )
    responsibility_1 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='मैं अपने श्रमिकों के जीवन की गुणवत्ता के लिए जिम्मेदार हूं।',
        widget=widgets.RadioSelect
    )
    responsibility_2 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='यह सुनिश्चित करना मेरी ज़िम्मेदारी है कि इस कारखाने में श्रमिकों को सुरक्षित और आरामदायक कार्यस्थल मिले।',
        widget=widgets.RadioSelect
    )
    responsibility_3 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='यह सुनिश्चित करना मेरी जिम्मेदारी है कि इस कारखाने के श्रमिकों को समय पर और पूरा भुगतान मिले।',
        widget=widgets.RadioSelect
    )
    responsibility_4 = models.StringField(
        choices=[['1','कभी नहीं'],['2','कभी-कभी'],
                 ['3','लगभग आधा समय'],['4','ज्यादातर'],['5','हमेशा']],
        label='यह सुनिश्चित करना मेरी जिम्मेदारी है कि इस कारखाने के श्रमिक उचित सरकारी योजनाओं के लिए पंजीकृत हों।',
        widget=widgets.RadioSelect
    )

# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age','gender','company','site','employer','owner','position', 'position_detail', 'company_experience', 'industry_experience']

class Workplace_Owner(Page):
    @staticmethod
    def is_displayed(player):
        return player.owner == '1'
    form_model = 'player'
    form_fields = ['workload','stress','fixed_mindset','teamwork','common_goals','competition']

class Workplace_Representative(Page):
    @staticmethod
    def is_displayed(player):
        return player.owner != '1'
    form_model = 'player'
    form_fields = ['workload','stress','fixed_mindset','teamwork','common_goals','competition','company_employee_relationship']

class Principal_Company_Owner(Page):
    @staticmethod
    def is_displayed(player):
        return player.owner == '1'
    form_model = 'player'
    form_fields = ['relationship_incentive','principal_company_approval_incentive','principal_company_disapproval_incentive','productivity_incentive','principal_company_trust']

class Principal_Company_Representative(Page):
    @staticmethod
    def is_displayed(player):
        return player.owner != '1'
    form_model = 'player'
    form_fields = ['relationship_incentive','principal_company_approval_incentive','principal_company_disapproval_incentive','productivity_incentive','principal_company_trust','interaction','decision_power']

class Principal_Company_Positive_Incentive_Details_Owner(Page):
    @staticmethod
    def is_displayed(player):
        return player.owner == '1' and player.principal_company_approval_incentive in ['4', '5']
    form_model = 'player'
    form_fields = ['respect','contract','increased_business','increased_payment','commendment_external','peer_acknowledgment', 'other_incentives']

class Principal_Company_Positive_Incentive_Details_Representative(Page):
    @staticmethod
    def is_displayed(player):
        return (player.owner != '1') and player.principal_company_approval_incentive in ['4', '5']
    form_model = 'player'
    form_fields = ['promotion','bonus','job_security', 'commendment_internal','respect','contract','increased_business','increased_payment','commendment_external','peer_acknowledgment', 'other_incentives']

class Principal_Company_Negative_Incentive_Details_Owner(Page):
    @staticmethod
    def is_displayed(player):
        return player.owner == '1'and player.principal_company_disapproval_incentive in ['4', '5']
    form_model = 'player'
    form_fields = ['respect_negative','contract_negative','increased_business_negative','increased_payment_negative','commendment_external_negative','peer_acknowledgment_negative', 'other_incentives_negative']

class Principal_Company_Negative_Incentive_Details_Representative(Page):
    @staticmethod
    def is_displayed(player):
        return (player.owner != '1') and player.principal_company_disapproval_incentive in ['4', '5']
    form_model = 'player'
    form_fields = ['promotion_negative','bonus_negative','job_security_negative', 'commendment_internal_negative','respect_negative','contract_negative','increased_business_negative','increased_payment_negative','commendment_external_negative','peer_acknowledgment_negative', 'other_incentives_negative']

class Worker(Page):
    form_model = 'player'
    form_fields = ['dehumanization_1','dehumanization_2','dehumanization_3','dehumanization_4','dehumanization_5','dehumanization_6','dehumanization_7','worker_motivation','worker_voice_attitudes','gender_leadership','gender_compliance','gender_norms',
                    'gender_productivity', 'geography_1','geography_2','caste_1','caste_2','worker_empathy_1','worker_empathy_2','responsibility_1','responsibility_2','responsibility_3','responsibility_4',]

class Thanks(Page):
    form_model = 'player'

page_sequence = [Demographics, Workplace_Owner, Workplace_Representative, Principal_Company_Owner,Principal_Company_Representative, Principal_Company_Positive_Incentive_Details_Owner, Principal_Company_Positive_Incentive_Details_Representative, Principal_Company_Negative_Incentive_Details_Owner,Principal_Company_Negative_Incentive_Details_Representative, Worker, Thanks]
