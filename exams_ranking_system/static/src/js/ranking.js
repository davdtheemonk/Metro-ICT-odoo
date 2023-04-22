odoo.define('exams_ranking_system.exam_ranking', function (require) {
    "use strict";

    var Widget = require('web.Widget');
    var session = require('web.session');
    var rpc = require('web.rpc');

    var ExamRankingWidget = Widget.extend({
        template: 'exams_ranking_system.exam_ranking',

        start: function () {
            var self = this;
            this._super.apply(this, arguments);

            // Fetch exam results from the server
            rpc.query({
                model: 'exams_ranking_system.examresult',
                method: 'search_read',
                args: [[], ['student_id', 'exam_id', 'marks_obtained']],
                kwargs: {context: session.user_context},
            }).then(function (results) {
                // Calculate ranking for each exam
                var rankings = {};
                _.each(results, function (result) {
                    var exam_id = result.exam_id[0];
                    if (!rankings[exam_id]) {
                        rankings[exam_id] = [];
                    }
                    rankings[exam_id].push(result);
                });
                _.each(rankings, function (results) {
                    results.sort(function (a, b) {
                        return b.marks_obtained - a.marks_obtained;
                    });
                    _.each(results, function (result, index) {
                        result.rank = index + 1;
                    });
                });

                // Render the ranking table
                self.$el.empty().append(QWeb.render('exams_ranking_system.exam_ranking_table', {
                    rankings: rankings,
                }));
            });
        },
    });

    return ExamRankingWidget;
});
