import React, { PureComponent } from 'react'
import PropTypes from 'prop-types'
import { Link } from 'react-router-dom'

class AppHeader extends PureComponent {

  static propTypes = {
    username: PropTypes.string.isRequired,
    onSignOut: PropTypes.func,
  }

  handleSignOut = (e) => {
    e.preventDefault()

    const { onSignOut } = this.props
    if (onSignOut) {
      onSignOut()
    }
  }

  render() {
    const { username } = this.props

    return (
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <span className="navbar-brand">Charibin</span>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarText">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item active">
              <Link className="nav-link" to="/">Home</Link>
            </li>
          </ul>
          <a className="navbar-text" href="/" onClick={this.handleSignOut}>
            Welcome, {username}!
          </a>
        </div>
      </nav>
    )
  }
}

export default AppHeader
