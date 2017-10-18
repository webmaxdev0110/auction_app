/*global FB:true*/

import React, { PureComponent } from 'react'
import { compose } from 'redux'
import { connect } from 'react-redux'
import { createStructuredSelector } from 'reselect'
import PropTypes from 'prop-types'

import AppLayout1 from 'pages/AppLayout1'
import SignUpForm from 'components/SignUpForm'
import { FACEBOOK_APP_ID, FACEBOOK_API_VERSION } from 'config'
import { signUp } from 'store/modules/auth'


class SignUp extends PureComponent {

  static propTypes = {
    signUp: PropTypes.func.isRequired,
  }

  state = {
    fbReady: false,
    signUpStatus: 0,
  }

  handleSubmit = (data) => {
    this.setState({
      signUpStatus: 1
    })

    this.props.signUp({
      data,
      success: () => this.setState({
        signUpStatus: 10
      }),
      fail: () => this.setState({
        signUpStatus: -1
      }),
    })
  }

  signUpWithFacebook = (event) => {
    event.preventDefault()

    if (!this.state.fbReady) {
      return
    }

    FB.login((response) => {
      if (response.status === 'connected') {
        this.props.history.push({
          pathname: `/signup-with-facebook/${response.authResponse.accessToken}`
        })
      }
    }, {
      scope: 'public_profile,email'
    })
  }

  componentDidMount() {
    window.fbAsyncInit = () => {
      FB.init({
        appId : FACEBOOK_APP_ID,
        cookie : true,
        xfbml : true,
        version : FACEBOOK_API_VERSION
      });
      
      this.setState({
        fbReady: true
      })
    };

    (function(d, s, id){
      var js, fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) {return;}
      js = d.createElement(s); js.id = id;
      js.src = "https://connect.facebook.net/en_US/sdk.js";
      fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
  }

  render() {
    const { fbReady, signUpStatus } = this.state

    return (
      <AppLayout1>
        <div className="container mt-5">
          <div className="row justify-content-center">
            <div className="col-12 col-md-8 col-lg-6">
              {
                signUpStatus === 10 ?
                <center>
                  You've successfully signed up a new account. Please check your email for account verification.
                </center>
                :
                <div>
                  <h3 className="mb-4 text-center">Sign Up</h3>

                  {signUpStatus === -1 && <div className="mb-2 text-danger">
                    Failed to sign up
                  </div>}

                  <SignUpForm onSubmit={this.handleSubmit} disabled={signUpStatus === 1} />

                  <center className="mt-2">
                    <a className={fbReady ? '' : 'text-muted'} href="/" onClick={this.signUpWithFacebook}>Sign Up With Facebook</a>
                  </center>

                </div>
              }
            </div>
          </div>
        </div>
      </AppLayout1>
    )
  }
}

const selector = createStructuredSelector({
})

const actions = {
  signUp,
}

export default compose(
  connect(selector, actions)
)(SignUp)
