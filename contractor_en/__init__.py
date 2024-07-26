from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'contractor_en'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1



class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #Demographics
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['0', 'Man'], ['1', 'Woman'], ['2', 'Transgender'], ['3',' Non-binary / Gender non-conforming'], ['4','Prefer not to say']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    company = models.StringField(label = 'Which principal company do you work at?')
    site = models.StringField(label = 'Which site do you work at? (If you work at multiple sites, please enter the site you are at right now)')
    employer = models.StringField(label = 'Which contractor do you work for?')
    owner = models.BooleanField(label='Are you the owner of your company?',
    )
    company_experience = models.IntegerField(
        label = 'How many full years have you worked for your company? If you have worked for this company less than one year, please enter 0', min = 0, max = 100
    )
    industry_experience = models.IntegerField(
        label = 'How many full years have you worked in this industry? If you have worked in this industry for less than one year, please enter 0', min = 0, max = 100
    )
    #Workplace 
    workload = models.StringField(
        choices=[['1','Often not enough to keep me busy'],['2','Sometimes not enough'],
                 ['3','Just the right amount'],['4','Sometimes too much'],['5','Entirely too much for me to handle']],
        label='How heavy was your workload during the last month?',
        widget=widgets.RadioSelect,
    )
    stress = models.StringField(
        choices=[['1','Never'],['2','Sometimes'],
                 ['3','About half the time'],['4','Most of the time'],['5','Always']],
        label='How often do you feel stressed, tense, restless, nervous or anxious, or unable to sleep at night because your mind is troubled?',
        widget=widgets.RadioSelect,
    )
    fixed_mindset = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='How much do you agree with the following statement: You can learn new things, but you can’t really change your basic intelligence.',
        widget=widgets.RadioSelect,
    )
    company_employee_relationship = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='How much do you agree with the following statement: If something is good for my company, it is also good for me.',
        widget=widgets.RadioSelect,
    )
    teamwork = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='How much do you agree with the following statement: The other contractors at this factory and I work well together.',
        widget=widgets.RadioSelect,
    )
    common_goals = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='How much do you agree with the following statement: The other contractors in this factory share the same goals as I do.',
        widget=widgets.RadioSelect,
    )
    competition = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='How much do you agree with the following statement: I want to ensure better working conditions and inclusive practices for my workers than other contractors provide for their workers.',
        widget=widgets.RadioSelect,
    )
    #Principal Company
    salience_perception = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label="The principal company cares about the quality of working conditions and inclusive practices for my workers.",
        widget=widgets.RadioSelect,
    )
    relationship_incentive = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label="The quality of the working conditions and inclusive practices I provide my workers significantly influences my company's contractual relationship with the principal company.",
        widget=widgets.RadioSelect,
    )
    principal_company_approval_incentive = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label="If I meet the principal company's expectations on working conditions and worker-inclusive practices, the principal company will be pleased with my company's performance.",
        widget=widgets.RadioSelect,
    )
    principal_company_disapproval_incentive = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label="If I do not meet the principal company's expectations on working conditions and worker-inclusive practices, the principal company will be displeased with my company's performance.",
        widget=widgets.RadioSelect,
    )
    productivity_incentive = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label="The principal company cares about the productivity of my company's workers.",
        widget=widgets.RadioSelect,
    )
    principal_company_trust = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='I trust the principal company to make decisions that will positively benefit my company.',
        widget=widgets.RadioSelect,
    )
    interaction_owner = models.StringField(
        choices=[['1','Only by me'],['2','Mostly by me'],
                 ['3','Equally by me and management'],['4','Mostly by management'],['5','Only by the management']],
        label="Is interaction with the prinicpal company primarily done by you or by your company's staff?",
        widget=widgets.RadioSelect,
    )
    decision_power_owner = models.StringField(
        choices=[['1','Only by me'],['2','Mostly by me'],
                 ['3','Equally by me and management'],['4','Mostly by management'],['5','Only by management']],
        label="Are business decisions regarding the relationship with the principal company primarily made by you or by your company's staff?",
        widget=widgets.RadioSelect,
    )
    interaction_rep = models.StringField(
        choices=[['1','Only by me'],['2','Mostly by me'],
                 ['3','Equally by me and management'],['4','Mostly by management'],['5','Only by the management']],
        label="Is interaction with the prinicpal company primarily done by you or by your company's management?",
        widget=widgets.RadioSelect,
    )
    decision_power_rep = models.StringField(
        choices=[['1','Only by me'],['2','Mostly by me'],
                 ['3','Equally by me and management'],['4','Mostly by management'],['5','Only by management']],
        label="Are business decisions regarding the relationship with the principal company primarily made by you or by your company's management?",
        widget=widgets.RadioSelect,
    )
    #Principal Company Positive Incentives Details
    promotion = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'I may be promoted faster.'
    )
    bonus = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'I may receive a bonus and/or reward.'
    )
    commendment_internal = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'My manager may commend my work.'
    )
    job_security = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'My job security may increase (I will be less worried about losing my job).'
    )
    respect = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'I may be more respected at work.'
    )
    contract = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = "The principal company may be more likely to renew my company's contract."
    )
    increased_business = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'The principal company may be more likely to hire my company at new sites.'
    )
    increased_payment = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'The principal company may be willing to pay my company more.'
    )
    commendment_external = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = "The principal company may commend my company's work."
    )
    peer_acknowledgment = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = "My company's acheivements may be acknowledged by other contractors."
    )
    other_incentives = models.StringField(
        label = "Please specify any other benefits you or your company may receive."
    )
    #Principal Company Negative Incentives Details
    promotion_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'My promotion prospects may be delayed.'
    )
    bonus_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'I may not receive a bonus or other reward that I would have otherwise received.'
    )
    job_security_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'My job security may decrease (I will be more worried about losing my job).'
    )
    commendment_internal_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'I may have a discussion with my manager about my performance.'
    )
    respect_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'I may be less respected at work.'
    )
    contract_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = "The principal company may be less likely to renew my company's contract."
    )
    increased_business_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'The principal company may be less likely to hire my company at new sites.'
    )
    increased_payment_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'The principal company may lower the fee it pays to my company.'
    )
    commendment_external_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'The principal company may have a discussion about my company about our/my performance.'
    )
    peer_acknowledgment_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'My company may be criticized by other contractors.'
    )
    other_incentives_negative = models.StringField(
        label = 'Please specify any other ramifications you or your company may face.'
    )    
    #Worker
    dehumanization_1 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='The workers in this factory are very intelligent.',
        widget=widgets.RadioSelect,
    )
    dehumanization_2 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='The workers in this factory do not think for themselves and must be told what to do.',
        widget=widgets.RadioSelect,
    )
    dehumanization_3 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='The workers in this factory do not understand complicated ideas.',
        widget=widgets.RadioSelect
    )
    dehumanization_4 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='The workers in this factory respond better to scolding than encouragement.',
        widget=widgets.RadioSelect
    )
    dehumanization_5 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='The workers in this factory are more productive if they feel comfortable and safe at work. ',
        widget=widgets.RadioSelect
    )
    dehumanization_6 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='The workers in this factory will not work hard unless we force them to.',
        widget=widgets.RadioSelect
    )
    dehumanization_7 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='Happy workers are more productive than unhappy workers.',
        widget=widgets.RadioSelect
    )
    worker_motivation = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='The workers in this factory are more motivated by money than by other rewards.',
        widget=widgets.RadioSelect
    ) 
    worker_voice_attitudes = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='Listening to worker feedback makes good business sense.',
        widget=widgets.RadioSelect
    )
    gender_leadership = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='In this factory, it is common for women to have leadership roles (e.g., as supervisors or managers).',
        widget=widgets.RadioSelect
    )
    gender_compliance = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='Adding women workers increases our responsibility and compliance requirements.',
        widget=widgets.RadioSelect
    )
    gender_norms = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='Since women have to cater to household work, they should not work in factories.',
        widget=widgets.RadioSelect
    )
    gender_productivity = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='Female workers are more productive than male workers in this factory.',
        widget=widgets.RadioSelect
    )
    geography_1 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='I find it easier to manage workers who come from the same state as I do.',
        widget=widgets.RadioSelect
    )
    geography_2 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='Migrant workers are more productive than local workers',
        widget=widgets.RadioSelect
    )
    caste_1 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='Our workers can get any job function, regardless of their caste.',
        widget=widgets.RadioSelect
    )
    caste_2 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='I find it a little difficult to interact with workers who come from different castes than mine.',
        widget=widgets.RadioSelect
    )
    worker_empathy_1 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='I think about the financial situation of my workers often.',
        widget=widgets.RadioSelect
    )
    worker_empathy_2 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='I find it easy to understand to the challenges my workers face.',
        widget=widgets.RadioSelect
    )
    responsibility_1 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='I am responsible for the quality of life of my workers.',
        widget=widgets.RadioSelect
    )
    responsibility_2 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='It is my responsibility to ensure the workers in this factory have a safe and comfortable workplace.',
        widget=widgets.RadioSelect
    )
    responsibility_3 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='It is my responsibility to ensure the workers in this factory receive timely and full payment.',
        widget=widgets.RadioSelect
    )
    responsibility_4 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='It is my responsibility to ensure the workers in this factory are regisitered for the appropriate government schemes.',
        widget=widgets.RadioSelect
    )
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age','gender','company','site','employer','owner', 'company_experience', 'industry_experience']

class Workplace_Owner(Page):
    @staticmethod
    def is_displayed(player):
        return player.owner
    form_model = 'player'
    form_fields = ['workload','stress','fixed_mindset','teamwork','common_goals','competition']

class Workplace_Representative(Page):
    @staticmethod
    def is_displayed(player):
        return not player.owner
    form_model = 'player'
    form_fields = ['workload','stress','fixed_mindset','teamwork','common_goals','competition','company_employee_relationship']

class Principal_Company_Owner(Page):
    @staticmethod
    def is_displayed(player):
        return player.owner
    form_model = 'player'
    form_fields = ['salience_perception','relationship_incentive','principal_company_approval_incentive','principal_company_disapproval_incentive','productivity_incentive','principal_company_trust', 'interaction_owner','decision_power_owner']

class Principal_Company_Representative(Page):
    @staticmethod
    def is_displayed(player):
        return not player.owner
    form_model = 'player'
    form_fields = ['salience_perception', 'relationship_incentive','principal_company_approval_incentive','principal_company_disapproval_incentive','productivity_incentive','principal_company_trust','interaction_rep','decision_power_rep']

class Principal_Company_Positive_Incentive_Details_Owner(Page):
    @staticmethod
    def is_displayed(player):
        return player.owner and player.principal_company_approval_incentive in ['4', '5']
    form_model = 'player'
    form_fields = ['respect','contract','increased_business','increased_payment','commendment_external','peer_acknowledgment', 'other_incentives']

class Principal_Company_Positive_Incentive_Details_Representative(Page):
    @staticmethod
    def is_displayed(player):
        return (not player.owner) and player.principal_company_approval_incentive in ['4', '5']
    form_model = 'player'
    form_fields = ['promotion','bonus','job_security', 'commendment_internal','respect','contract','increased_business','increased_payment','commendment_external','peer_acknowledgment', 'other_incentives']

class Principal_Company_Negative_Incentive_Details_Owner(Page):
    @staticmethod
    def is_displayed(player):
        return player.owner and player.principal_company_disapproval_incentive in ['4', '5']
    form_model = 'player'
    form_fields = ['respect_negative','contract_negative','increased_business_negative','increased_payment_negative','commendment_external_negative','peer_acknowledgment_negative', 'other_incentives_negative']

class Principal_Company_Negative_Incentive_Details_Representative(Page):
    @staticmethod
    def is_displayed(player):
        return (not player.owner) and player.principal_company_disapproval_incentive in ['4', '5']
    form_model = 'player'
    form_fields = ['promotion_negative','bonus_negative','job_security_negative', 'commendment_internal_negative','respect_negative','contract_negative','increased_business_negative','increased_payment_negative','commendment_external_negative','peer_acknowledgment_negative', 'other_incentives_negative']

class Worker(Page):
    form_model = 'player'
    form_fields = ['dehumanization_1','dehumanization_2','dehumanization_3','dehumanization_4','dehumanization_5','dehumanization_6','dehumanization_7','worker_motivation','worker_voice_attitudes','gender_leadership','gender_compliance','gender_norms',
                    'gender_productivity', 'geography_1','geography_2','caste_1','caste_2','worker_empathy_1','worker_empathy_2','responsibility_1','responsibility_2','responsibility_3','responsibility_4',]

class Thanks(Page):
    form_model = 'player'

page_sequence = [Demographics, Workplace_Owner, Workplace_Representative, Principal_Company_Owner,Principal_Company_Representative, Principal_Company_Positive_Incentive_Details_Owner, Principal_Company_Positive_Incentive_Details_Representative, Principal_Company_Negative_Incentive_Details_Owner,Principal_Company_Negative_Incentive_Details_Representative, Worker, Thanks]
