describe('Home Page/Index Tests', () => {
    // Page Load Test
    it('successfully loads', () => {
        cy.visit('/');
        cy.url().should('include', '/');
    });

    // Address Tests
    it('disables find button when new user visits site', () => {
        cy.get('button.find-button').should('be.disabled');
    });

    it('enables find button upon a valid address being entered or selected', () => {
        cy.get('input#address').type('22 Shelbourne Road', { force: true }).focus();
        cy.get('.pac-item').first().click();
        cy.get('button.find-button').should('not.be.disabled');
    });

    it('disables find button if input is empty', () => {
        cy.get('input#address').clear({ force: true });
        cy.get('button.find-button').should('be.disabled', { force: true });
    });

    it('returns to homepage and display error if "Dublin" is not in address', () => {
        cy.get('input#address').clear({ force: true }).type('Cork', { force: true }).get('input#address').focus();
        cy.get('.pac-item').first().click().wait(1000);
        cy.get('#address-finder').submit().wait(1000);
        cy.url().should('equal', 'http://127.0.0.1:8000/');
        cy.get('.toast').should('have.class', 'show');
        cy.get('.toast-header').children('strong').should('contain', 'Error');
        cy.get('.toast-body').children().should('contain', 'Address not found within Dublin, please try again');
    });

    it('redirects to all restaurants page and display "Dublin" as address if no address inputted and cuisine selected', () => {
        cy.get('i.fa-pizza-slice').click();
        cy.url().should('include', 'restaurants').should('contain', 'cuisine=pizza');
        cy.get('h4.nearby-restaurants').should('contain', 'delivering in Dublin');
        cy.get('.change-location > a').should('contain', 'set location');
    });

    it('redirects to all restaurants page and display valid address on page if valid address', () => {
        cy.visit('/');
        cy.get('input#address').clear({ force: true }).type('22 Shelbourne Road', { force: true }).focus();
        cy.get('.pac-item').first().click().wait(1000);
        cy.get('#address-finder').submit().wait(1000);
        cy.url().should('equal', 'http://127.0.0.1:8000/restaurants/');
        cy.get('h4.nearby-restaurants').should('contain', 'delivering to 22 Shelbourne Road');
        cy.get('.change-location > a').should('contain', 'change location');
    });
});