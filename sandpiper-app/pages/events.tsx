import React from 'react'
import styled from 'styled-components';

import Breadcrumb from 'react-bootstrap/Breadcrumb';

import { BodyContainer, BreadcrumbContainer } from '../components/containers';

const BreadcrumbEvents= () => {
  return (
    <Breadcrumb>
      <Breadcrumb.Item href="/">Home</Breadcrumb.Item>
      <Breadcrumb.Item active>Events</Breadcrumb.Item>
    </Breadcrumb>
  );
}

const Events = () => {
  return (
  <BodyContainer>
    <BreadcrumbContainer>
      <BreadcrumbEvents/>
    </BreadcrumbContainer>

    Events go here
  </BodyContainer>
  )
}

export default Events