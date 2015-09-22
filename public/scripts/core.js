$(document).ready(function () {
    window.ImageModel = Backbone.Model.extend({
        defaults: {
            src: null,
            alt: null,
            caption: null
        }
    });


    window.ImageCollection = Backbone.Collection.extend({
        model: ImageModel,
        selectedImage: null
    });


    window.ExpandedImageView = Backbone.View.extend({
        template: _.template('<div class="big-image"><img src="<%= src %>" alt="<%= alt %>"/><div class="img-caption"><%= caption %></div></div>'),
        initialize: function () {
            this.collection.selectedImage = this.collection.at(0);
            this.collection.on('change', this.render, this);
            this.render();
        },

        render: function () {
            this.$el.html(this.template(this.collection.selectedImage.attributes));
        }
    });


    window.MiniImagesView = Backbone.View.extend({
        template: _.template('<% _.each(images, function(image) { %><div class="thumbnail-image<% if (selectedImage == image) { %> selected<% } %>"><img src="<%= image.get("src") %>" alt="<%= image.get("alt") %>"/></div><% }); %>'),
        events: {
            'click .thumbnail-image': 'changeSelected'
        },
        initialize: function () {
            this.collection.on('change', this.render, this);
            this.render();
        },

        changeSelected: function (evt) {
            var selectedModel = this.collection.at($(evt.currentTarget).index());
            this.collection.selectedImage = selectedModel;
            this.collection.trigger('change');
        },

        render: function () {
            this.$el.html(this.template({images: this.collection.models, selectedImage: this.collection.selectedImage}));
        }
    });
});