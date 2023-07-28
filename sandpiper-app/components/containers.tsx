import styled from 'styled-components';
import { colors } from '../styles/colors';

export const BodyContainer = styled.div`
  padding: 10px 20px;
  height: 100vh;

  div::-webkit-scrollbar {
    height: 0.75rem;
  }

  div::-webkit-scrollbar-track {
    background: ${colors.lightGrey30};
    border-radius: 1px;
  }
  div::-webkit-scrollbar-thumb {
    background: ${colors.lightGrey};
    border-radius: 1px;
  }

  div::-webkit-scrollbar-thumb:hover {
    background: ${colors.darkGrey};
  }
`

export const BreadcrumbContainer = styled.div`
  & nav > ol > .breadcrumb-item.active {
    color: ${colors.lightGrey};
  }

  & nav > ol > .breadcrumb-item.active::before {
    color: ${colors.lightGrey};
  }

  & nav > ol > li > a {
    color: ${colors.baseColor};
  }

  & nav > .breadcrumb {
    --bs-breadcrumb-margin-bottom: 0rem;
  }
`
