window.homecomponent = {
    route: '/',
    template: /* html */ `
    <section>
      <h1>Home</h1>
      <p>{{ welcomeMessage }}</p>
    </section>
    `,
    data() {
        // data() returns the values this component can use in its template.
        return {
            user: null,
            welcomeMessage: 'Welcome home!'
        };
    },
    async mounted() {
        // mounted() runs after the component has been inserted into the page.
        if (this.user) {
            this.welcomeMessage = `Welcome ${this.user.name}!`;
            return;
        }

        try {
            // Vue does not replace fetch; we can still use normal browser APIs.
            const reply = await fetch('/user');
            if (reply.status === 200) {
                this.user = await reply.json();
                this.welcomeMessage = `Welcome ${this.user.name}!`;
            }
        } catch (error) {
            console.log(error);
        }
    }
};