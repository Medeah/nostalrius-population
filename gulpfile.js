'use strict';

var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');

gulp.task('javascript', function() {
  // Minify and copy all JavaScript (except vendor scripts)
  // with sourcemaps all the way down
  return gulp.src(['node_modules/jquery-flot/jquery.flot.js',
                    'node_modules/jquery-flot/jquery.flot.time.js',
                    'node_modules/jquery-flot/jquery.flot.selection.js',
                    'node_modules/timezone-js/src/date.js',
                    'app.js'])
    .pipe(uglify())
    .pipe(concat('all.min.js'))
    .pipe(gulp.dest('static'));
});
