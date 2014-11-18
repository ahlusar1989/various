Router.configure({
  layoutTemplate: 'base'
});

Router.route('/', function () {
  this.render('projects');
});

Router.route('/signIn', function () {
  this.render('signIn');
});

Router.route('/signUp', function () {
  this.render('signUp');
});

Router.route('/projects', function () {
  this.render('projects');
});

Router.route('/employees', function () {
  this.render('employees');
});
