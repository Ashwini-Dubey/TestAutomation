/// <reference types="cypress" />

describe ('API Automation - GET Method', () =>
{
    let accessToken = '0dca8de44b53f262d13eb6e8d85f82c75eb345ff8771b7072959b57b6a81ccd7'

    it('Get details of all the users', () => {
            cy.request({
                method : 'GET',
                url : 'https://gorest.co.in/public-api/users',
                headers : {
                    'authorization' : 'Bearer ' + accessToken
                }
            })
            .should((Response) => {
                cy.log(JSON.stringify(Response.body))
            
            expect(Response.status).to.eq(200)
            expect(Response.body.meta.pagination.limit).to.eq(10)
        })
    })

    
    it('Get details of all the users based on user id', () => {
            cy.request({
                method : 'GET',
                url : 'https://gorest.co.in/public-api/users/2',
                headers : {
                    'authorization' : 'Bearer ' + accessToken
                }
            })
            .should((Response) => {
                cy.log(JSON.stringify(Response.body))
            
            expect(Response.status).to.eq(200)
            expect(Response.body.data.name).to.include('Prayag')
            expect(Response.body.data.id).to.eq(2)
        })
    })

})