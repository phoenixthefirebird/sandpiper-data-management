import styled from 'styled-components';
import Table from 'react-bootstrap/Table';

import { colors } from '../styles/colors';

export const StyledTable = styled(Table)`
  --bs-table-border-color: ${colors.lightGrey};
  --bs-table-striped-bg: ${colors.lightGrey15};
  --bs-table-hover-bg: ${colors.lightGrey30};
  --bs-table-color: ${colors.darkGrey};
  --bs-table-striped-color: ${colors.darkGrey};
  --bs-table-active-color: ${colors.darkGrey};
  --bs-table-hover-color: ${colors.darkGrey};
`
