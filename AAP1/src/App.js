import * as React from 'react';
import {createAppContainer} from 'react-navigation';
import {createStackNavigator} from 'react-navigation-stack';
import ProfileAndPreferences from './Profile';
import lastName from './lastName';
import PhoneNumber from './Phone';
import PayPal from './PayPal';
import jobSearch from './jobSearch';
import JobDetail from './JobDetail';
import Calendar from './Calendar';
import ProcessingJob from './ProcessingJob';
import Home from './Home';
import firstName from './firstName';
import Address from './Address';
import Bio from './Bio';
import JobList from './JobList';
import jobHistory from './jobHistory';

const RootStack = createStackNavigator(
  {
    Home: Home,
    jobHistory: jobHistory,
    ProfileAndPreferences: ProfileAndPreferences,
    firstName: firstName,
    lastName: lastName,
    PhoneNumber: PhoneNumber,
    PayPal: PayPal,
    jobSearch: jobSearch,
    Calendar: Calendar,
    JobDetail: JobDetail,
    ProcessingJob: ProcessingJob,
    Address: Address,
    Bio: Bio,
    JobList: JobList,
  },
  {
    initialRouteName: 'Home',
  },
);

const AppContainer = createAppContainer(RootStack);

export default class App extends React.Component {
  render() {
    return <AppContainer />;
  }
}
