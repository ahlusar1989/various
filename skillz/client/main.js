Session.setDefault('DOWNTIME', false);
Session.setDefault('APPNAME', 'Skillbase');
Session.setDefault('SHOWPROJECTFORM', false);
Session.setDefault('SHOWEMPLOYEEFORM', false);
Session.setDefault('EDITING_PROJECT', null);
Session.setDefault('EDITING_EMPLOYEE', null);

Handlebars.registerHelper("formatDate", function(datetime) {
  if (moment) {
    return moment(datetime).format("DD/MM/YYYY");
  } else {
    return datetime;
  }
});

Template.base.helpers({
  DOWNTIME: function(){
    return Session.get('DOWNTIME');
  }
});

Template.navbar.helpers({
  APPNAME: function(){
    return Session.get('APPNAME');
  }
});

Template.sidebar.helpers({
  activeIfTemplateIs: function (template) {
    var currentRoute = Router.current();
    return currentRoute &&
      template === currentRoute.lookupTemplate() ? 'active' : '';
  }
});

Template.comingsoon.helpers({
  days: function(){
    return Session.get('days');
  },
  hours: function(){
    return Session.get('hours');
  },
  mins: function(){
    return Session.get('mins');
  },
  secs: function(){
    return Session.get('secs');
  },       
});

// Authentication helpers
trimInput = function(value) {
    return value.replace(/^\s*|\s*$/g, '');
};

isNotEmpty = function(value) {
    if (value && value !== ''){
        return true;
    }
    Session.set('alert', 'Please fill in all required fields.');
    return false;
};

isEmail = function(value) {
    var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (filter.test(value)) {
        return true;
    }
    Session.set('alert', 'Please enter a valid email address.');
    return false;
};

isValidPassword = function(password) {
    if (password.length < 6) {
        Session.set('alert', 'Your password should be 6 characters or longer.');
        return false;
    }
    return true;
};

areValidPasswords = function(password, confirm) {
    if (!isValidPassword(password)) {
        return false;
    }
    if (password !== confirm) {
        Session.set('alert', 'Your two passwords are not equivalent.');
        return false;
    }
    return true;
};  

Template.alert.helpers({
    alert: function() {
        return Session.get('alert');
    }
});

Template.signUp.events({
    'submit #signUpForm': function(event, template) {
        event.preventDefault();

        var signUpForm = $(event.currentTarget),
            email = trimInput(signUpForm.find('#signUpEmail').val().toLowerCase()),
            password = signUpForm.find('#signUpPassword').val(),
            passwordConfirm = signUpForm.find('#signUpPasswordConfirm').val();

        if (isNotEmpty(email) && isNotEmpty(password) && isEmail(email) && areValidPasswords(password, passwordConfirm)) {
            Accounts.createUser({email: email, password: password}, function(err) {
                if (err) {
                    if (err.message === 'Email already exists. [403]') {
                        Session.set('alert', 'We\'re sorry but this email is already used.');
                    } else {
                        Session.set('alert', 'We\'re sorry but something went wrong.');
                    }
                } else {
                    Session.set('alert', 'Congrats! You\'re now a new Meteorite!');
                }
            });
        }
        return false;
    },
});

Template.signOut.events({
    'click #signOut': function(event, template) {
        Meteor.logout(function() {
            Session.set('alert', 'Bye Meteorite! Come back whenever you want!');
        });
        return false;
    }
});

Template.signIn.events({
    'submit #signInForm': function(event, template) {
        event.preventDefault();

        var signInForm = $(event.currentTarget),
            email = trimInput(signInForm.find('.email').val().toLowerCase()),
            password = signInForm.find('.password').val();

        if (isNotEmpty(email) && isEmail(email) && isNotEmpty(password) && isValidPassword(password)) {
            Meteor.loginWithPassword(email, password, function(err) {
                if (err) {
                    Session.set('alert', 'We\'re sorry but these credentials are not valid.');
                } else {
                    Sesson.set('alert', 'Welcome back New Meteorite!');
                }
            });
        }
        return false;
    },
    'click #showForgotPassword': function(event, template) {
        Session.set('showForgotPassword', true);
        return false;
    },
});

Template.main.helpers({
    showForgotPassword: function() {
        return Session.get('showForgotPassword');
    },
    resetPassword: function(){
        return Session.get('resetPassword');
    }    
});

Template.forgotPassword.events({
    'submit #forgotPasswordForm': function(event, template) {
        event.preventDefault();

        var forgotPasswordForm = $(event.currentTarget),
            email = trimInput(forgotPasswordForm.find('#forgotPasswordEmail').val().toLowerCase());

        if (isNotEmpty(email) && isEmail(email)) {
            Accounts.forgotPassword({email: email}, function(err) {
                if (err) {
                    if (err.message === 'User not found [403]') {
                        Session.set('alert', 'This email does not exist.');
                    } else {
                        Session.set('alert', 'We\'re sorry but something went wrong.');
                    }
                } else {
                    Session.set('alert', 'Email Sent. Please check your mailbox to reset your password.');
                }
            });
        }
        return false;
    },

    'click #returnToSignIn': function(event, template) {
        Session.set('showForgotPassword', null);
        return false;
    },
});

if (Accounts._resetPasswordToken) {
    Session.set('resetPassword', Accounts._resetPasswordToken);
}

Template.resetPassword.events({
    'submit #resetPasswordForm': function(event, template) {
        event.preventDefault();
        
        var resetPasswordForm = $(event.currentTarget),
            password = resetPasswordForm.find('#resetPasswordPassword').val(),
            passwordConfirm = resetPasswordForm.find('#resetPasswordPasswordConfirm').val();

        if (isNotEmpty(password) && areValidPasswords(password, passwordConfirm)) {
            Accounts.resetPassword(Session.get('resetPassword'), password, function(err) {
                if (err) {
                    Session.set('alert', {type: 'error', message: 'We\'re sorry but something went wrong.'});
                }
                else {
                    Session.set('alert', 'Your password has been changed. Welcome back!');
                    Session.set('resetPassword', null);
                }
            });
        }
        return false;
    }
}); 

// Admin helpers
// Projects
Template.projects.helpers({
  projectList: function(){
    return Projects.find();
  },
  SHOWPROJECTFORM: function(){
    return Session.get('SHOWPROJECTFORM');
  },
  EDITING_PROJECT: function(){
    return Session.get('EDITING_PROJECT');
  },
});

Template.projectRow.helpers({
  selected: function () {
    return Session.equals("EDITING_PROJECT", this._id) ? "selected" : '';
  }       
});

Template.projects.events({
  'click .addProject':function(event, template){
    Session.set('SHOWPROJECTFORM',true);
  }
});

Template.projectRow.events({
    'click .projectRow':function(event, template){
      Session.set('EDITING_PROJECT',template.data._id);
      Session.set('SHOWPROJECTFORM',true);
  }
}); 

Template.projectForm.helpers({
  employees: function(){
    return Employees.find();
  },
  project: function(){
    return Projects.findOne({_id:Session.get('EDITING_PROJECT')});
  },
  SHOWPROJECTFORM: function(){
    return Session.get('SHOWPROJECTFORM');
  },
  EDITING_PROJECT: function(){
    return Session.get('EDITING_PROJECT');
  },        
});

Template.projectForm.events({
  'click .save':function(event, template){
    var name = template.find('.name').value;
    var client = template.find('.client').value;
    var status = template.find('.status').value;
    var owner = template.find('.owner').value;
    var datedue = template.find('.datedue').value;

    if(Session.get('EDITING_PROJECT')){
      updateProject(name,client,status,owner,datedue);
    } else{
      addProject(name,client,status,owner,datedue); 
    }
    Session.set('SHOWPROJECTFORM',false);
    Session.set('EDITING_PROJECT',null);
  },
  'click .close':function(event, template){
    Session.set('SHOWPROJECTFORM',false);
  },
  'click .cancel':function(event, template){
    Session.set('SHOWPROJECTFORM',false);
    Session.set('EDITING_PROJECT',null);
  },
  'click .remove':function(event, template){
    removeProject();  
    Session.set('SHOWPROJECTFORM',false);
    Session.set('EDITING_PROJECT',null);
  }
});

var addProject = function(name,client,status,ownerid,datedue){
  if(ownerid){
    owner = Employees.findOne({_id:ownerid});
  } else{
    owner = null;
  }
  Projects.insert({name:name,client:client,status:status,owner:owner,datedue:datedue});
}

var updateProject = function(name,client,status,ownerid,datedue){
  if(ownerid){
    owner = Employees.findOne({_id:ownerid});
  } else{
    owner = null;
  }
  Projects.update(Session.get('EDITING_PROJECT'), {$set: {name:name,client:client,status:status,owner:owner,datedue:datedue}});
  return true;
}

var removeProject = function(){
  Projects.remove({_id:Session.get('EDITING_PROJECT')});
}
// Projects


// Employees
Template.employees.helpers({
  employeeList: function(){
    return Employees.find();
  },
  EDITING_EMPLOYEE: function(){
    return Session.get('EDITING_EMPLOYEE');
  },
  SHOWEMPLOYEEFORM: function(){
    return Session.get('SHOWEMPLOYEEFORM');
  }     
});

Template.employees.events({
  'click .addEmployee':function(event, template){
    Session.set('SHOWEMPLOYEEFORM',true);
  }
});

Template.employeeRow.events({
  'click .employeeRow':function(event, template){
    Session.set('EDITING_EMPLOYEE',template.data._id);
    Session.set('SHOWEMPLOYEEFORM',true);
  }
});

Template.employeeForm.helpers({
  employee: function(){
    if(Session.get('EDITING_EMPLOYEE')){
      return Employees.findOne({_id:Session.get('EDITING_EMPLOYEE')});
    }
  },
  SHOWEMPLOYEEFORM: function(){
    return Session.get('SHOWEMPLOYEEFORM');
  },
  EDITING_EMPLOYEE: function(){
    return Session.get('EDITING_EMPLOYEE');
  },        
});

Template.employeeForm.events({
  'click .save':function(event, template){
    var name = template.find('.name').value;
    if(Session.get('EDITING_EMPLOYEE')){
      updateEmployee(Session.get('EDITING_EMPLOYEE'),name);
    } else{
      addEmployee(name);
    }
    Session.set('SHOWEMPLOYEEFORM',false);
  },
  'click .cancel':function(event, template){
    Session.set('SHOWEMPLOYEEFORM',false);
  },
  'click .close':function(event, template){
    Session.set('SHOWEMPLOYEEFORM',false);
  },
  'click .remove':function(event, template){
    removeEmployee(); 
    Session.set('SHOWEMPLOYEEFORM',false);
    Session.set('EDITING_PROJECT',null);    
  }
});

var addEmployee = function(name){
  Employees.insert({name:name});
  return true;
}

var updateEmployee = function(id,name){
  Employees.update(id, {$set: {name:name}});
  return true;
}

var removeEmployee = function(){
  Employees.remove({_id:Session.get('EDITING_EMPLOYEE')});
}
// Employees

// Timer
setDate = function(){

  var launch = new Date(2014, 12, 25, 00, 00);  
  
  var now = new Date();
  var s = -now.getTimezoneOffset()*60 + (launch.getTime() - now.getTime())/1000;

  var d = Math.floor(s/86400);
  if (d != Session.get('days')){
    Session.set('days', d)
  }
  s -= d*86400;

  var h = Math.floor(s/3600);
  if (h != Session.get('hours')){
    Session.set('hours', h)
  }
  s -= h*3600;

  var m = Math.floor(s/60);
  if (m != Session.get('mins')){
    Session.set('mins', m)
  }

  s = Math.floor(s-m*60);
  if (s != Session.get('secs')){
    Session.set('secs', s)
  }
      
};

Meteor.setInterval(setDate, 1000);

