import React from 'react'
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import styled from 'styled-components';
import { colors } from '../styles/colors';

import Breadcrumb from 'react-bootstrap/Breadcrumb';

import { BodyContainer, BreadcrumbContainer } from '../components/containers';


const BreadcrumbHome= () => {
  return (
    <Breadcrumb>
      <Breadcrumb.Item active>Home</Breadcrumb.Item>
    </Breadcrumb>
  );
}

const StyledButton = styled(Button)`
  --bs-btn-color: ${colors.baseColor};
  --bs-btn-border-color: ${colors.baseColor};
  --bs-btn-hover-color: #fff;
  --bs-btn-hover-bg: ${colors.baseColor};
  --bs-btn-hover-border-color: ${colors.baseColor};
  --bs-btn-focus-shadow-rgb: 13,110,253;
  --bs-btn-active-color: #fff;
  --bs-btn-active-bg: ${colors.baseColor};
  --bs-btn-active-border-color: ${colors.baseColor};
  --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  --bs-btn-disabled-color: ${colors.baseColor};
  --bs-btn-disabled-bg: transparent;
  --bs-btn-disabled-border-color: ${colors.baseColor};
  --bs-gradient: none;
`

const OptionsContainer = styled.div`
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
`

const OptionContainer = styled.div`
  display: flex;
  flex-direction: column;
  gap: 1rem;
  align-items: center;
  justify-content: center;
`


const Home = () => {
  return (
    <BodyContainer>
      <OptionsContainer>
        
        <OptionContainer>
          <img src='/icons/profiles.svg' alt='an icon containing three people, symbolizes a crowd'/>
          <StyledButton href="/profiles" variant="outline-primary" size="lg">
            Profiles
          </StyledButton>
        </OptionContainer>

        <OptionContainer>
          <img src='/icons/events.svg' alt='a calendar with a star on it, symbolizes event'/>
          <StyledButton href="/events" variant="outline-primary" size="lg">
            Events
          </StyledButton>
        </OptionContainer>

      </OptionsContainer>
    </BodyContainer>
  )
}

export default Home