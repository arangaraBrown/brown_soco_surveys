from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'supervisor'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1



class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(
        label='Do you consent to participate in this survey?',
    )
    #Demographics
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['0', 'Man'], ['1', 'Woman'], ['2', 'Transgender'], ['3',' Non-binary / Gender non-conforming'], ['4','Prefer not to say']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    position = models.StringField(
        label = 'What is your job title? Please note that if you have more than one job title we are interested in the title or responsibilities that you regard as the most important.'
    )
    position_detail = models.StringField(
        label = 'Please describe your role in more detail.'
    )
    company_experience = models.IntegerField(
        label = 'How many years have you worked for this company?', min = 0, max = 100
    )
    industry_experience = models.IntegerField(
        label = 'How many years have you worked in this industry?', min = 0, max = 100
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
    teamwork = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='How much do you agree with the following statement: The other supervisors at this factory and I work well together.',
        widget=widgets.RadioSelect,
    )
    common_goals = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='How much do you agree with the following statement: The other supervisors in this factory share the same goals as I do.',
        widget=widgets.RadioSelect,
    )
    competition = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='How much do you agree with the following statement: I want to treat the workers I supervise better than other supervisors do.',
        widget=widgets.RadioSelect,
    )
    #Manager
    career_incentive = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='The way I treat workers significantly influences my career trajectory within this company.',
        widget=widgets.RadioSelect,
    )
    management_approval_incentive = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='If I treat the workers I supervise well, my manager will be pleased with my performance',
        widget=widgets.RadioSelect,
    )
    management_disapproval_incentive = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='If I treat the workers I supervise badly, my manager will be displeased with my performance',
        widget=widgets.RadioSelect,
    )
    productivity_incentive = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='My manager cares about the productivity of the workers I supervise.',
        widget=widgets.RadioSelect,
    )
    quality_incentive = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='My manager cares about the quality of work the workers I supervise produce.',
        widget=widgets.RadioSelect,
    )
    manager_trust = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='I trust my manager to make decisions that will positively benefit me.',
        widget=widgets.RadioSelect,
    )
    #Manager Positive Incentives Details
    promotion = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'I may be promoted faster.'
    )
    bonus = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'I may recieve a bonus and/or reward.'
    )
    commendment = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'My manager might commend my work.'
    )
    peer_acknowledgment = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'My achievements may be acknowledged by other supervisors.'
    )
    job_security = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'My job security may increase (I will be less worried about losing my job).'
    )
    respect = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'I may be more respected at work.'
    )
    other_incentives = models.StringField(
        label = 'Please specify any other benefits you may receive if your manager is pleased with your performance.'
    )
    #Manager Negative Incentives Details
    promotion_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'My promotion prospects may be delayed.'
    )
    bonus_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'I may not receive a bonus or other reward that I would have otherwise received.'
    )
    commendment_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'I may have a required discussion with my manager about my performance.'
    )
    peer_acknowledgment_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'I may be criticized by other supervisors.'
    )
    job_security_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'My job security may decrease (I will be more worried about losing my job).'
    )
    respect_negative = models.StringField(
        choices = [['0', 'No'],['1','Yes']],
        label = 'I may be less respected at work.'
    )
    other_incentives_negative = models.StringField(
        label = 'Please specify any other benefits you may receive if your manager is displeased with your performance.'
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
    gender_norms = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='Since women have to cater to household work, they should not work in factories.',
        widget=widgets.RadioSelect
    )
    harrassment = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='In this factory, it’s common for supervisors or managers to make sexual comments to or try to sexually touch workers. .',
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
        label='Caste-based job functions can be completely eliminated from the shopfloor.',
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
        label='I think about the financial situation of the workers I supervise often.',
        widget=widgets.RadioSelect
    )
    worker_empathy_2 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='I find it easy to understand to the challenges the workers I supervise face.',
        widget=widgets.RadioSelect
    )
    responsibility_1 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='I am responsible for the quality of life of the workers I supervise.',
        widget=widgets.RadioSelect
    )
    responsibility_2 = models.StringField(
        choices=[['1','Strongly Disagree'],['2','Somewhat Disagree'],
                 ['3','Neither agree nor disagree'],['4','Somewhat Agree'],['5','Strongly Agree']],
        label='It is my responsibility to ensure the workers I supervise have a safe and comfortable workplace.',
        widget=widgets.RadioSelect
    )
    # Factory Outcomes Perceptions
    productivity_perceptions_1 = models.StringField(
        choices=[['1','YES, more comfortable working conditions are linked to LOWER productivity.'],['2','YES, more comfortable working conditions are linked to HIGHER productivity.'],
                 ['3','NO, there’s no relationship.'],],
        label='Do you believe that there is a relationship between productivity and working conditions in this factory?',
        widget=widgets.RadioSelect
    )
    productivity_perceptions_2 = models.StringField(
        choices=[['1','YES, when workers have peace of mind they are LESS productive.'],['2','YES, when workers have peace of mind they are MORE productive.'],
                 ['3','NO, there’s no relationship.'],],
        label="Do you think there is a relationship between workers' peace of mind and their productivity?",
        widget=widgets.RadioSelect
    )
    quality_perceptions_1 = models.StringField(
        choices=[['1','YES, when workers have peace of mind their work is LOWER quality.'],['2','YES, when workers have peace of mind their work is HIGHER quality.'],
                 ['3','NO, there’s no relationship.'],],
        label="Do you think there is a relationship between workers' peace of mind and the quality of their work?",
        widget=widgets.RadioSelect
    )
    

# PAGES
class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

class Demographics(Page):
    @staticmethod
    def is_displayed(player):
        return player.consent
    form_model = 'player'
    form_fields = ['age','gender','position', 'position_detail', 'company_experience', 'industry_experience']

class Workplace(Page):
    @staticmethod
    def is_displayed(player):
        return player.consent
    form_model = 'player'
    form_fields = ['workload','stress','fixed_mindset','teamwork','common_goals','competition']

class Manager(Page):
    @staticmethod
    def is_displayed(player):
        return player.consent
    form_model = 'player'
    form_fields = ['career_incentive','management_approval_incentive','management_disapproval_incentive','productivity_incentive','quality_incentive','manager_trust']

class Manager_Positive_Incentive_Details(Page):
    @staticmethod
    def is_displayed(player):
        return (player.consent and (player.management_approval_incentive == '4' or player.management_approval_incentive == '5'))
    form_model = 'player'
    form_fields = ['promotion','bonus','commendment', 'peer_acknowledgment', 'job_security', 'respect','other_incentives']

class Manager_Negative_Incentive_Details(Page):
    @staticmethod
    def is_displayed(player):
        return (player.consent and (player.management_disapproval_incentive == '4' or player.management_disapproval_incentive == '5'))
    form_model = 'player'
    form_fields = ['promotion_negative','bonus_negative','commendment_negative', 'peer_acknowledgment_negative', 'job_security_negative', 'respect_negative','other_incentives_negative']

class Worker(Page):
    @staticmethod
    def is_displayed(player):
        return player.consent
    form_model = 'player'
    form_fields = ['dehumanization_1','dehumanization_2','dehumanization_3','dehumanization_4','dehumanization_5','dehumanization_6','dehumanization_7','worker_motivation','worker_voice_attitudes','gender_leadership','gender_norms',
                   'gender_productivity','harrassment', 'geography_1','geography_2','caste_1','caste_2','worker_empathy_1','worker_empathy_2','responsibility_1','responsibility_2', ]

class Factory_Outcomes(Page):
    @staticmethod
    def is_displayed(player):
        return player.consent
    form_model = 'player'
    form_fields = ['productivity_perceptions_1','productivity_perceptions_2','quality_perceptions_1',]


class Thanks(Page):
    form_model = 'player'


page_sequence = [Consent, Demographics, Workplace, Manager, Manager_Positive_Incentive_Details,Manager_Negative_Incentive_Details, Worker, Factory_Outcomes, Thanks]
