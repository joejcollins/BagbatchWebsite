''' Routes for the main/home pages '''
from flask import render_template, Blueprint
 
################
#### config ####
################
home_blueprint = Blueprint('home', __name__, template_folder='templates')
 
 
################
#### routes ####
################
 
@home_blueprint.route('/')
def index():
    return render_template('index.html')

@home_blueprint.route('email', methods=['GET', 'POST'])
def form():
    ''' Show the message form for the user to fill in '''
    message_form = forms.MessageForm()
    if message_form.validate_on_submit():
        send_mail(message_form.email.data, message_form.message.data)
        return render_template('submitted_form.html', title="Thanks", form=message_form)
    return render_template('form.html', title="Message", form=message_form)

def send_mail(their_email, their_message):
    ''' Send an email message to me '''
    message = mail.EmailMessage(sender=app_identity.get_application_id() +
                                '@appspot.gserviceaccount.com>')
    message.subject = 'Message from Bagbatch Website'
    message.to = Settings.get('EMAIL')
    message.body = """From: {}\n\n<<BEGINS>>\n\n{}\n\n<<ENDS>>""".format(their_email, their_message)
    message.send()
    