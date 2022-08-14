/// <reference types="cypress" />

describe ('API Automation - Restful Booker', () =>
{
    context('Get Booking Ids of all the bookings', () => {
        it('GET Request', () => {
            cy.request({
                method : 'GET',
                url : 'https://gorest.co.in/public-api/users',
                headers : {
                    'authorization' : 'Bearer 0dca8de44b53f262d13eb6e8d85f82c75eb345ff8771b7072959b57b6a81ccd7'
                }
            })
            .should((Response) => {
                cy.log(JSON.stringify(Response.body))
            
            expect(Response.status).to.eq(200)
            expect(Response.body.meta.pagination.limit).to.eq(10)
            })
        })
    })

    context('Get Booking Ids of all the bookings', () => {
        it('GET Request', () => {
            cy.request({
                method : 'GET',
                url : 'https://gorest.co.in/public-api/users/2',
                headers : {
                    'authorization' : 'Bearer 0dca8de44b53f262d13eb6e8d85f82c75eb345ff8771b7072959b57b6a81ccd7'
                }
            })
            .should((Response) => {
                cy.log(JSON.stringify(Response.body))
            
            expect(Response.status).to.eq(200)
            })
        })
    })

})