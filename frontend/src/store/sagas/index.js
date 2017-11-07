import { all } from 'redux-saga/effects'

import auth from './auth'
import adminCharities from './admin/charities'
import adminDonors from './admin/donors'
import adminProducts from './admin/products'
import adminAuctions from './admin/auctions'
import adminTags from './admin/tags'
import adminUsers from './admin/users'
import adminMedia from './admin/media'
import account from './account'
import auctions from './auctions'
import donors from './donors'
import jobs from './jobs'
import settings from './settings'


export default function* rootSaga() {
  yield all([
    auth(),
    adminCharities(),
    adminDonors(),
    adminProducts(),
    adminAuctions(),
    adminTags(),
    adminUsers(),
    adminMedia(),
    account(),
    auctions(),
    donors(),
    jobs(),
    settings()
  ])
}
