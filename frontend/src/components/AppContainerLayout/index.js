import React, { PureComponent } from 'react'


class AppContainerLayout extends PureComponent {
  render() {
    const { children } = this.props

    return (
      <div className="container py-5 my-5">
        {children}
      </div>
    )
  }
}

export default AppContainerLayout