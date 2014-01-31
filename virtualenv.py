




<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>virtualenv/virtualenv.py at develop · pypa/virtualenv · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="pypa/virtualenv" name="twitter:title" /><meta content="virtualenv - Virtual Python Environment builder" name="twitter:description" /><meta content="https://0.gravatar.com/avatar/097e00640790ef99fa4df9e0c29cc6d8?d=https%3A%2F%2Fidenticons.github.com%2F45c2ed3e6e691d8e6bef302fcb4f5ff9.png&amp;r=x&amp;s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://0.gravatar.com/avatar/097e00640790ef99fa4df9e0c29cc6d8?d=https%3A%2F%2Fidenticons.github.com%2F45c2ed3e6e691d8e6bef302fcb4f5ff9.png&amp;r=x&amp;s=400" property="og:image" /><meta content="pypa/virtualenv" property="og:title" /><meta content="https://github.com/pypa/virtualenv" property="og:url" /><meta content="virtualenv - Virtual Python Environment builder" property="og:description" />

    <meta name="hostname" content="github-fe127-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 2.1.0p0-github-tcmalloc (87d8860372) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035/">
    <link rel="xhr-socket" href="/_sockets" />
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="C0EDDB60:5591:34E604A:52EBD8C7" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="fXxUU2HpJ2ZD52HoxzdPf4eGTX5UjUyfbaapIuAlRiE=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-b4cefd115535acdd2560c36100dc32e7e36c5285.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-b60d21b9ec8ae7d4b5c6f190d0cbddbccfccfe50.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://github.global.ssl.fastly.net/assets/frameworks-3e59bf2ccf0be318d5d920c2ab0bf1ab4cb3a96b.js" type="text/javascript"></script>
      <script async="async" defer="defer" src="https://github.global.ssl.fastly.net/assets/github-f8309e5c7f6feecd392527ff43751b2e7014135d.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="3b6b292bc5d61dcca830bcf2f8ed9385">

        <link data-pjax-transient rel='permalink' href='/pypa/virtualenv/blob/de06f2085487c969fa5efb1ed03860128e58d7e1/virtualenv.py'>

  <meta name="description" content="virtualenv - Virtual Python Environment builder" />

  <meta content="647025" name="octolytics-dimension-user_id" /><meta content="pypa" name="octolytics-dimension-user_login" /><meta content="1446474" name="octolytics-dimension-repository_id" /><meta content="pypa/virtualenv" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="1446474" name="octolytics-dimension-repository_network_root_id" /><meta content="pypa/virtualenv" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/pypa/virtualenv/commits/develop.atom" rel="alternate" title="Recent Commits to virtualenv:develop" type="application/atom+xml" />

  </head>


  <body class="logged_out  env-production  vis-public page-blob">
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2Fpypa%2Fvirtualenv%2Fblob%2Fdevelop%2Fvirtualenv.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="pypa/virtualenv"
      data-branch="develop"
      data-sha="ad997b9849401719a95feadf09485a6194bdea74"
  >

    <input type="hidden" name="nwo" value="pypa/virtualenv" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>


      


          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
    <a href="/login?return_to=%2Fpypa%2Fvirtualenv"
    class="minibutton with-count js-toggler-target star-button tooltipped upwards"
    title="You must be signed in to use this feature" rel="nofollow">
    <span class="octicon octicon-star"></span>Star
  </a>

    <a class="social-count js-social-count" href="/pypa/virtualenv/stargazers">
      814
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fpypa%2Fvirtualenv"
        class="minibutton with-count js-toggler-target fork-button tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/pypa/virtualenv/network" class="social-count">
        220
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/pypa" class="url fn" itemprop="url" rel="author"><span itemprop="title">pypa</span></a>
          </span>
          <span class="repohead-name-divider">/</span>
          <strong><a href="/pypa/virtualenv" class="js-current-repository js-repo-home-link">virtualenv</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      

      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped leftwards" title="Code">
        <a href="/pypa/virtualenv" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /pypa/virtualenv">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped leftwards" title="Issues">
          <a href="/pypa/virtualenv/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /pypa/virtualenv/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>184</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped leftwards" title="Pull Requests">
        <a href="/pypa/virtualenv/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /pypa/virtualenv/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>29</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/pypa/virtualenv/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /pypa/virtualenv/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/pypa/virtualenv/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /pypa/virtualenv/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/pypa/virtualenv/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /pypa/virtualenv/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/pypa/virtualenv.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/pypa/virtualenv.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/pypa/virtualenv" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/pypa/virtualenv" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="octicon help tooltipped upwards" title="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>



                <a href="/pypa/virtualenv/archive/develop.zip"
                   class="minibutton sidebar-button"
                   title="Download this repository as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:0592a28ee3f7f1a55cb3a48931a4ce5b -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/pypa/virtualenv/find/develop" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="develop"
    data-ref="develop"
    role="button" aria-label="Switch branches or tags" tabindex="0">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">develop</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/blob/1.9.X/virtualenv.py"
                 data-name="1.9.X"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.9.X">1.9.X</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/blob/1.10.X/virtualenv.py"
                 data-name="1.10.X"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.10.X">1.10.X</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/blob/1.11.X/virtualenv.py"
                 data-name="1.11.X"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.11.X">1.11.X</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/blob/bugfix-lib64-symlink-full-path/virtualenv.py"
                 data-name="bugfix-lib64-symlink-full-path"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="bugfix-lib64-symlink-full-path">bugfix-lib64-symlink-full-path</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/blob/develop/virtualenv.py"
                 data-name="develop"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="develop">develop</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/blob/docs_test/virtualenv.py"
                 data-name="docs_test"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="docs_test">docs_test</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/blob/master/virtualenv.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/blob/upgrade-pip-distlib/virtualenv.py"
                 data-name="upgrade-pip-distlib"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="upgrade-pip-distlib">upgrade-pip-distlib</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.11rc4/virtualenv.py"
                 data-name="1.11rc4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.11rc4">1.11rc4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.11rc3/virtualenv.py"
                 data-name="1.11rc3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.11rc3">1.11rc3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.11rc2/virtualenv.py"
                 data-name="1.11rc2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.11rc2">1.11rc2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.11rc1/virtualenv.py"
                 data-name="1.11rc1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.11rc1">1.11rc1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.11.2/virtualenv.py"
                 data-name="1.11.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.11.2">1.11.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.11.1rc2/virtualenv.py"
                 data-name="1.11.1rc2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.11.1rc2">1.11.1rc2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.11.1rc1/virtualenv.py"
                 data-name="1.11.1rc1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.11.1rc1">1.11.1rc1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.11.1/virtualenv.py"
                 data-name="1.11.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.11.1">1.11.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.11/virtualenv.py"
                 data-name="1.11"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.11">1.11</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.10rc10/virtualenv.py"
                 data-name="1.10rc10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.10rc10">1.10rc10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.10rc9/virtualenv.py"
                 data-name="1.10rc9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.10rc9">1.10rc9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.10rc8/virtualenv.py"
                 data-name="1.10rc8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.10rc8">1.10rc8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.10rc7/virtualenv.py"
                 data-name="1.10rc7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.10rc7">1.10rc7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.10rc6/virtualenv.py"
                 data-name="1.10rc6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.10rc6">1.10rc6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.10rc5/virtualenv.py"
                 data-name="1.10rc5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.10rc5">1.10rc5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.10rc4/virtualenv.py"
                 data-name="1.10rc4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.10rc4">1.10rc4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.10rc3/virtualenv.py"
                 data-name="1.10rc3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.10rc3">1.10rc3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.10rc2/virtualenv.py"
                 data-name="1.10rc2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.10rc2">1.10rc2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.10rc1/virtualenv.py"
                 data-name="1.10rc1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.10rc1">1.10rc1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.10.1/virtualenv.py"
                 data-name="1.10.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.10.1">1.10.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.10/virtualenv.py"
                 data-name="1.10"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.10">1.10</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.9rc2/virtualenv.py"
                 data-name="1.9rc2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.9rc2">1.9rc2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.9rc1/virtualenv.py"
                 data-name="1.9rc1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.9rc1">1.9rc1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.9.1/virtualenv.py"
                 data-name="1.9.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.9.1">1.9.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.9/virtualenv.py"
                 data-name="1.9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.9">1.9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.8.4/virtualenv.py"
                 data-name="1.8.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.8.4">1.8.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.8.3/virtualenv.py"
                 data-name="1.8.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.8.3">1.8.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.8.2/virtualenv.py"
                 data-name="1.8.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.8.2">1.8.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.8.1/virtualenv.py"
                 data-name="1.8.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.8.1">1.8.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.8/virtualenv.py"
                 data-name="1.8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.8">1.8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.7.2/virtualenv.py"
                 data-name="1.7.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.7.2">1.7.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.7.1.2/virtualenv.py"
                 data-name="1.7.1.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.7.1.2">1.7.1.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.7.1.1/virtualenv.py"
                 data-name="1.7.1.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.7.1.1">1.7.1.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.7.1/virtualenv.py"
                 data-name="1.7.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.7.1">1.7.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.7/virtualenv.py"
                 data-name="1.7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.7">1.7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.6.4/virtualenv.py"
                 data-name="1.6.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.6.4">1.6.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.6.3/virtualenv.py"
                 data-name="1.6.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.6.3">1.6.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.6.2/virtualenv.py"
                 data-name="1.6.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.6.2">1.6.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.6.1/virtualenv.py"
                 data-name="1.6.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.6.1">1.6.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.6/virtualenv.py"
                 data-name="1.6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.6">1.6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.5.2/virtualenv.py"
                 data-name="1.5.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.5.2">1.5.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.5.1/virtualenv.py"
                 data-name="1.5.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.5.1">1.5.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.5/virtualenv.py"
                 data-name="1.5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.5">1.5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.4.9/virtualenv.py"
                 data-name="1.4.9"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.4.9">1.4.9</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.4.8/virtualenv.py"
                 data-name="1.4.8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.4.8">1.4.8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.4.6/virtualenv.py"
                 data-name="1.4.6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.4.6">1.4.6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.4.3/virtualenv.py"
                 data-name="1.4.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.4.3">1.4.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.4.2/virtualenv.py"
                 data-name="1.4.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.4.2">1.4.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.4.1/virtualenv.py"
                 data-name="1.4.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.4.1">1.4.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.4/virtualenv.py"
                 data-name="1.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.4">1.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.3.4/virtualenv.py"
                 data-name="1.3.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.3.4">1.3.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.3.3/virtualenv.py"
                 data-name="1.3.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.3.3">1.3.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.3.2/virtualenv.py"
                 data-name="1.3.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.3.2">1.3.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.3.1/virtualenv.py"
                 data-name="1.3.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.3.1">1.3.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.3/virtualenv.py"
                 data-name="1.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.3">1.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/pypa/virtualenv/tree/1.2/virtualenv.py"
                 data-name="1.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.2">1.2</a>
            </div> <!-- /.select-menu-item -->
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/pypa/virtualenv" data-branch="develop" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">virtualenv</span></a></span></span><span class="separator"> / </span><strong class="final-path">virtualenv.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="virtualenv.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  <div class="commit file-history-tease">
    <img alt="Donald Stufft" class="main-avatar" height="24" src="https://1.gravatar.com/avatar/ebf132362b622423ed5baca2988911b8?d=https%3A%2F%2Fidenticons.github.com%2Fafd3da353ee2dfc81b0b0c95738ff9c6.png&amp;r=x&amp;s=140" width="24" />
    <span class="author"><a href="/dstufft" rel="author">dstufft</a></span>
    <time class="js-relative-date" datetime="2014-01-20T19:50:45-08:00" title="2014-01-20 19:50:45">January 20, 2014</time>
    <div class="commit-title">
        <a href="/pypa/virtualenv/commit/e578a632a8dbc0818ab63dde84688769cf630b52" class="message" data-pjax="true" title="Merge branch &#39;master&#39; into develop

Conflicts:
	virtualenv.py">Merge branch 'master' into develop</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>80</strong> contributors</a></p>
          <a class="avatar tooltipped downwards" title="ianb" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=ianb"><img alt="Ian Bicking" height="20" src="https://0.gravatar.com/avatar/cc8334869c9d2a9e603017f2da805eb3?d=https%3A%2F%2Fidenticons.github.com%2F58caf27a48e7930aefd5437298d64a70.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="jezdez" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=jezdez"><img alt="Jannis Leidel" height="20" src="https://1.gravatar.com/avatar/cf3595fa166bfb4106211e1697f39f94?d=https%3A%2F%2Fidenticons.github.com%2Fa14ac55a4f27472c5d894ec1c3c743d2.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="carljm" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=carljm"><img alt="Carl Meyer" height="20" src="https://1.gravatar.com/avatar/b1f36e554be0e1ae19f9a74d6ece9107?d=https%3A%2F%2Fidenticons.github.com%2Fe482800024b39046c2083659c4191614.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="pfmoore" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=pfmoore"><img alt="Paul Moore" height="20" src="https://0.gravatar.com/avatar/d995b462a98fea412efa79d17ba3787a?d=https%3A%2F%2Fidenticons.github.com%2F38c70c2015c60372a0b1970db78f876b.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="qwcode" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=qwcode"><img alt="Marcus Smith" height="20" src="https://0.gravatar.com/avatar/54a4bb3eb0b5992f52fd516196d9c83d?d=https%3A%2F%2Fidenticons.github.com%2Fcafbbff742a748b370a1f35322317d9b.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="antocuni" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=antocuni"><img alt="antocuni" height="20" src="https://1.gravatar.com/avatar/cdc3cafa377f0e0e93fc69636021ef65?d=https%3A%2F%2Fidenticons.github.com%2Fc0ba87c8463e246b003d20c231a05a3c.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="pjenvey" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=pjenvey"><img alt="Philip Jenvey" height="20" src="https://0.gravatar.com/avatar/ef0ed749a263aeefda2a47789f998c1c?d=https%3A%2F%2Fidenticons.github.com%2Fdd4143061640d55fb312dd0ce8afa76e.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="pnasrat" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=pnasrat"><img alt="Paul Nasrat" height="20" src="https://2.gravatar.com/avatar/bed78e60d7f5c6985dd0273c880812cf?d=https%3A%2F%2Fidenticons.github.com%2Fa84f33ae6490fe0c1335b1b5180d92fa.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="dstufft" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=dstufft"><img alt="Donald Stufft" height="20" src="https://1.gravatar.com/avatar/ebf132362b622423ed5baca2988911b8?d=https%3A%2F%2Fidenticons.github.com%2Fafd3da353ee2dfc81b0b0c95738ff9c6.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="ejucovy" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=ejucovy"><img alt="ejucovy" height="20" src="https://2.gravatar.com/avatar/7b8260c0cc5d2728d4e538bcc43cf432?d=https%3A%2F%2Fidenticons.github.com%2F8c57c059b482aab74ca9f368dc9da524.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="g2p" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=g2p"><img alt="Gabriel de Perthuis" height="20" src="https://1.gravatar.com/avatar/2d151f7205a2cf6641b503c67b9565e0?d=https%3A%2F%2Fidenticons.github.com%2F106a232c3d4318f606c7f8e970a80f5a.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="gthb" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=gthb"><img alt="Gunnlaugur Thor Briem" height="20" src="https://1.gravatar.com/avatar/e2326aa08224115dd8724ff6c1c7f2ee?d=https%3A%2F%2Fidenticons.github.com%2F8a411025f66661e44d5bd17d7a0781fb.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="k0s" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=k0s"><img alt="Jeff Hammel" height="20" src="https://1.gravatar.com/avatar/a4648ac4d203974259823c1f1630496a?d=https%3A%2F%2Fidenticons.github.com%2F20538ad79aa9bd2e620d9b146836d6be.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="deniscostadsc" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=deniscostadsc"><img alt="Denis Costa" height="20" src="https://0.gravatar.com/avatar/ca2b5813ded9633f64cf1e276dd0e9dd?d=https%3A%2F%2Fidenticons.github.com%2Fc0e8d35e265b600ef166d2025fcfc1cf.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="otherchirps" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=otherchirps"><img alt="Chris Nilsson" height="20" src="https://0.gravatar.com/avatar/61aad7aa6e8cff40e22f420015d5aee9?d=https%3A%2F%2Fidenticons.github.com%2F77d62051c2a93d809e3d298cf84f641d.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="alexandrul" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=alexandrul"><img alt="Eduard-Cristian Stefan" height="20" src="https://2.gravatar.com/avatar/74a9c07c5b31b883768def1c4eb78782?d=https%3A%2F%2Fidenticons.github.com%2Fbbecd3a681f8ddee6f3d43df7af2b575.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="jaraco" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=jaraco"><img alt="Jason R. Coombs" height="20" src="https://0.gravatar.com/avatar/163acaf31cfd01645493404a2d379df6?d=https%3A%2F%2Fidenticons.github.com%2Fee5b05407f845fb22224d269563fe882.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="CBWhiz" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=CBWhiz"><img alt="CBWhiz" height="20" src="https://0.gravatar.com/avatar/40992d33a3ec2698aabd5f7694338174?d=https%3A%2F%2Fidenticons.github.com%2F7799e74b730426413a6d07ef0011a777.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="bcarl" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=bcarl"><img alt="Brandon Carl" height="20" src="https://0.gravatar.com/avatar/7dc73cfba121ad974341e6f1c21bb717?d=https%3A%2F%2Fidenticons.github.com%2F55aadb3565012742638fe512599fd1a5.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="vhata" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=vhata"><img alt="Jonathan Hitchcock" height="20" src="https://2.gravatar.com/avatar/2a0f736473bce688cf89dccd1486959f?d=https%3A%2F%2Fidenticons.github.com%2F94dd3eabb51db7d9c2ea86f62a143f64.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="msabramo" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=msabramo"><img alt="Marc Abramowitz" height="20" src="https://1.gravatar.com/avatar/3d91a2f54a0ad7f3044458a064ea7a84?d=https%3A%2F%2Fidenticons.github.com%2F0d145b716defe62e054bf09c2e78a9e4.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="jpenney" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=jpenney"><img alt="Jason Penney" height="20" src="https://1.gravatar.com/avatar/9d5d6abc8894300f88f82b2df42a5faf?d=https%3A%2F%2Fidenticons.github.com%2F6f6a5d78eef0f75fd5bc78c22c6a6dff.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="kisielk" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=kisielk"><img alt="Kamil Kisiel" height="20" src="https://0.gravatar.com/avatar/55fd56dfef815d7aa543be09ad3ed3e9?d=https%3A%2F%2Fidenticons.github.com%2F1c5db5f26705c8dc6cc16c97f85a6ad9.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="vbabiy" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=vbabiy"><img alt="Vitaly Babiy" height="20" src="https://2.gravatar.com/avatar/7639090fe1ef7c934691a5ecb7083a7d?d=https%3A%2F%2Fidenticons.github.com%2Fb33ab78dc0e9072a05258918507b3e6f.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="gutworth" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=gutworth"><img alt="Benjamin Peterson" height="20" src="https://2.gravatar.com/avatar/cd2e442c42c95ed534e4197df4300222?d=https%3A%2F%2Fidenticons.github.com%2Fc5fa39d263ca38801d5efb33b6afe3d9.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="elpargo" href="/pypa/virtualenv/commits/develop/virtualenv.py?author=elpargo"><img alt="Jorge Vargas" height="20" src="https://2.gravatar.com/avatar/a57c52861cb36307efbb477b4ec3a292?d=https%3A%2F%2Fidenticons.github.com%2Fee90403891c6321aae860594914e28e2.png&amp;r=x&amp;s=140" width="20" /></a>

      <a href="#blob_contributors_box" rel="facebox" class="others-text">and others.</a>

    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="Ian Bicking" height="24" src="https://0.gravatar.com/avatar/cc8334869c9d2a9e603017f2da805eb3?d=https%3A%2F%2Fidenticons.github.com%2F58caf27a48e7930aefd5437298d64a70.png&amp;r=x&amp;s=140" width="24" />
            <a href="/ianb">ianb</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Jannis Leidel" height="24" src="https://1.gravatar.com/avatar/cf3595fa166bfb4106211e1697f39f94?d=https%3A%2F%2Fidenticons.github.com%2Fa14ac55a4f27472c5d894ec1c3c743d2.png&amp;r=x&amp;s=140" width="24" />
            <a href="/jezdez">jezdez</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Carl Meyer" height="24" src="https://1.gravatar.com/avatar/b1f36e554be0e1ae19f9a74d6ece9107?d=https%3A%2F%2Fidenticons.github.com%2Fe482800024b39046c2083659c4191614.png&amp;r=x&amp;s=140" width="24" />
            <a href="/carljm">carljm</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Paul Moore" height="24" src="https://0.gravatar.com/avatar/d995b462a98fea412efa79d17ba3787a?d=https%3A%2F%2Fidenticons.github.com%2F38c70c2015c60372a0b1970db78f876b.png&amp;r=x&amp;s=140" width="24" />
            <a href="/pfmoore">pfmoore</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Marcus Smith" height="24" src="https://0.gravatar.com/avatar/54a4bb3eb0b5992f52fd516196d9c83d?d=https%3A%2F%2Fidenticons.github.com%2Fcafbbff742a748b370a1f35322317d9b.png&amp;r=x&amp;s=140" width="24" />
            <a href="/qwcode">qwcode</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="antocuni" height="24" src="https://1.gravatar.com/avatar/cdc3cafa377f0e0e93fc69636021ef65?d=https%3A%2F%2Fidenticons.github.com%2Fc0ba87c8463e246b003d20c231a05a3c.png&amp;r=x&amp;s=140" width="24" />
            <a href="/antocuni">antocuni</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Philip Jenvey" height="24" src="https://0.gravatar.com/avatar/ef0ed749a263aeefda2a47789f998c1c?d=https%3A%2F%2Fidenticons.github.com%2Fdd4143061640d55fb312dd0ce8afa76e.png&amp;r=x&amp;s=140" width="24" />
            <a href="/pjenvey">pjenvey</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Paul Nasrat" height="24" src="https://2.gravatar.com/avatar/bed78e60d7f5c6985dd0273c880812cf?d=https%3A%2F%2Fidenticons.github.com%2Fa84f33ae6490fe0c1335b1b5180d92fa.png&amp;r=x&amp;s=140" width="24" />
            <a href="/pnasrat">pnasrat</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Donald Stufft" height="24" src="https://1.gravatar.com/avatar/ebf132362b622423ed5baca2988911b8?d=https%3A%2F%2Fidenticons.github.com%2Fafd3da353ee2dfc81b0b0c95738ff9c6.png&amp;r=x&amp;s=140" width="24" />
            <a href="/dstufft">dstufft</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="ejucovy" height="24" src="https://2.gravatar.com/avatar/7b8260c0cc5d2728d4e538bcc43cf432?d=https%3A%2F%2Fidenticons.github.com%2F8c57c059b482aab74ca9f368dc9da524.png&amp;r=x&amp;s=140" width="24" />
            <a href="/ejucovy">ejucovy</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Gabriel de Perthuis" height="24" src="https://1.gravatar.com/avatar/2d151f7205a2cf6641b503c67b9565e0?d=https%3A%2F%2Fidenticons.github.com%2F106a232c3d4318f606c7f8e970a80f5a.png&amp;r=x&amp;s=140" width="24" />
            <a href="/g2p">g2p</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Gunnlaugur Thor Briem" height="24" src="https://1.gravatar.com/avatar/e2326aa08224115dd8724ff6c1c7f2ee?d=https%3A%2F%2Fidenticons.github.com%2F8a411025f66661e44d5bd17d7a0781fb.png&amp;r=x&amp;s=140" width="24" />
            <a href="/gthb">gthb</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Jeff Hammel" height="24" src="https://1.gravatar.com/avatar/a4648ac4d203974259823c1f1630496a?d=https%3A%2F%2Fidenticons.github.com%2F20538ad79aa9bd2e620d9b146836d6be.png&amp;r=x&amp;s=140" width="24" />
            <a href="/k0s">k0s</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Denis Costa" height="24" src="https://0.gravatar.com/avatar/ca2b5813ded9633f64cf1e276dd0e9dd?d=https%3A%2F%2Fidenticons.github.com%2Fc0e8d35e265b600ef166d2025fcfc1cf.png&amp;r=x&amp;s=140" width="24" />
            <a href="/deniscostadsc">deniscostadsc</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Chris Nilsson" height="24" src="https://0.gravatar.com/avatar/61aad7aa6e8cff40e22f420015d5aee9?d=https%3A%2F%2Fidenticons.github.com%2F77d62051c2a93d809e3d298cf84f641d.png&amp;r=x&amp;s=140" width="24" />
            <a href="/otherchirps">otherchirps</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Eduard-Cristian Stefan" height="24" src="https://2.gravatar.com/avatar/74a9c07c5b31b883768def1c4eb78782?d=https%3A%2F%2Fidenticons.github.com%2Fbbecd3a681f8ddee6f3d43df7af2b575.png&amp;r=x&amp;s=140" width="24" />
            <a href="/alexandrul">alexandrul</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Jason R. Coombs" height="24" src="https://0.gravatar.com/avatar/163acaf31cfd01645493404a2d379df6?d=https%3A%2F%2Fidenticons.github.com%2Fee5b05407f845fb22224d269563fe882.png&amp;r=x&amp;s=140" width="24" />
            <a href="/jaraco">jaraco</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="CBWhiz" height="24" src="https://0.gravatar.com/avatar/40992d33a3ec2698aabd5f7694338174?d=https%3A%2F%2Fidenticons.github.com%2F7799e74b730426413a6d07ef0011a777.png&amp;r=x&amp;s=140" width="24" />
            <a href="/CBWhiz">CBWhiz</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Brandon Carl" height="24" src="https://0.gravatar.com/avatar/7dc73cfba121ad974341e6f1c21bb717?d=https%3A%2F%2Fidenticons.github.com%2F55aadb3565012742638fe512599fd1a5.png&amp;r=x&amp;s=140" width="24" />
            <a href="/bcarl">bcarl</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Jonathan Hitchcock" height="24" src="https://2.gravatar.com/avatar/2a0f736473bce688cf89dccd1486959f?d=https%3A%2F%2Fidenticons.github.com%2F94dd3eabb51db7d9c2ea86f62a143f64.png&amp;r=x&amp;s=140" width="24" />
            <a href="/vhata">vhata</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Marc Abramowitz" height="24" src="https://1.gravatar.com/avatar/3d91a2f54a0ad7f3044458a064ea7a84?d=https%3A%2F%2Fidenticons.github.com%2F0d145b716defe62e054bf09c2e78a9e4.png&amp;r=x&amp;s=140" width="24" />
            <a href="/msabramo">msabramo</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Jason Penney" height="24" src="https://1.gravatar.com/avatar/9d5d6abc8894300f88f82b2df42a5faf?d=https%3A%2F%2Fidenticons.github.com%2F6f6a5d78eef0f75fd5bc78c22c6a6dff.png&amp;r=x&amp;s=140" width="24" />
            <a href="/jpenney">jpenney</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Kamil Kisiel" height="24" src="https://0.gravatar.com/avatar/55fd56dfef815d7aa543be09ad3ed3e9?d=https%3A%2F%2Fidenticons.github.com%2F1c5db5f26705c8dc6cc16c97f85a6ad9.png&amp;r=x&amp;s=140" width="24" />
            <a href="/kisielk">kisielk</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Vitaly Babiy" height="24" src="https://2.gravatar.com/avatar/7639090fe1ef7c934691a5ecb7083a7d?d=https%3A%2F%2Fidenticons.github.com%2Fb33ab78dc0e9072a05258918507b3e6f.png&amp;r=x&amp;s=140" width="24" />
            <a href="/vbabiy">vbabiy</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Benjamin Peterson" height="24" src="https://2.gravatar.com/avatar/cd2e442c42c95ed534e4197df4300222?d=https%3A%2F%2Fidenticons.github.com%2Fc5fa39d263ca38801d5efb33b6afe3d9.png&amp;r=x&amp;s=140" width="24" />
            <a href="/gutworth">gutworth</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Jorge Vargas" height="24" src="https://2.gravatar.com/avatar/a57c52861cb36307efbb477b4ec3a292?d=https%3A%2F%2Fidenticons.github.com%2Fee90403891c6321aae860594914e28e2.png&amp;r=x&amp;s=140" width="24" />
            <a href="/elpargo">elpargo</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Stefano Rivera" height="24" src="https://1.gravatar.com/avatar/c7b8ae95ff9a611e2139262e7c98b376?d=https%3A%2F%2Fidenticons.github.com%2F4aa755c051f0932c006c0878ac28bad3.png&amp;r=x&amp;s=140" width="24" />
            <a href="/stefanor">stefanor</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Wang Xuerui" height="24" src="https://2.gravatar.com/avatar/bc3d38d961c654b44fb084a4411d94f4?d=https%3A%2F%2Fidenticons.github.com%2F03a8f955424fa40138a95dc052c7d87c.png&amp;r=x&amp;s=140" width="24" />
            <a href="/xen0n">xen0n</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Brian Rosner" height="24" src="https://2.gravatar.com/avatar/b7472bc7aa45c70641c299e9408b78ab?d=https%3A%2F%2Fidenticons.github.com%2Fc8ffe9a587b126f152ed3d89a146b445.png&amp;r=x&amp;s=140" width="24" />
            <a href="/brosner">brosner</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Barry Warsaw" height="24" src="https://2.gravatar.com/avatar/01aa7d6d4db83982a2f6dd363d0ee0f3?d=https%3A%2F%2Fidenticons.github.com%2F4e669e791e7d76f66e7209bce06fed76.png&amp;r=x&amp;s=140" width="24" />
            <a href="/warsaw">warsaw</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Chris Adams" height="24" src="https://0.gravatar.com/avatar/f5934485a0863578733c447016505547?d=https%3A%2F%2Fidenticons.github.com%2F93de42b079dbd3509c11c6ce85d823c1.png&amp;r=x&amp;s=140" width="24" />
            <a href="/acdha">acdha</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Piotr Dobrogost" height="24" src="https://2.gravatar.com/avatar/497ee9d231fba5446f89cb85c5efba1d?d=https%3A%2F%2Fidenticons.github.com%2F431d817803444a1c513dcc7e66b3c901.png&amp;r=x&amp;s=140" width="24" />
            <a href="/piotr-dobrogost">piotr-dobrogost</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Jürgen Hermann" height="24" src="https://1.gravatar.com/avatar/24a0d33f5b812dbc1d62aea831cdc387?d=https%3A%2F%2Fidenticons.github.com%2Fcf99eaa570985989926a064397ddda81.png&amp;r=x&amp;s=140" width="24" />
            <a href="/jhermann">jhermann</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="" height="24" src="https://2.gravatar.com/avatar/cab5fca74e84a6941ad18381b54c01d2?d=https%3A%2F%2Fidenticons.github.com%2Fc94987188429dd2aab9a16ae610aa775.png&amp;r=x&amp;s=140" width="24" />
            <a href="/jab">jab</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="jkleint" height="24" src="https://identicons.github.com/182dc59bec3f2517c9272ad451529241.png" width="24" />
            <a href="/jkleint">jkleint</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Kumar McMillan" height="24" src="https://0.gravatar.com/avatar/3e7e975f0fa432f4ae6604f72c132309?d=https%3A%2F%2Fidenticons.github.com%2F01074d0e0ca64dd52127d542d631eef0.png&amp;r=x&amp;s=140" width="24" />
            <a href="/kumar303">kumar303</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Kyle Gibson" height="24" src="https://1.gravatar.com/avatar/1b8ac3c112c5e74eb4abecea021d818f?d=https%3A%2F%2Fidenticons.github.com%2F12eef684d5c79ca628f9225b25d3785e.png&amp;r=x&amp;s=140" width="24" />
            <a href="/kylegibson">kylegibson</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Gregory Haskins" height="24" src="https://1.gravatar.com/avatar/0f38df3d16a2b141b68d2d2db57c2d7a?d=https%3A%2F%2Fidenticons.github.com%2F940951a5aeeba5b4444910d3b07765d2.png&amp;r=x&amp;s=140" width="24" />
            <a href="/greghaskins">greghaskins</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Graham Dennis" height="24" src="https://0.gravatar.com/avatar/c1ec9369a8985feefc185a64206c1d7c?d=https%3A%2F%2Fidenticons.github.com%2F12ddaea6b76b46c7e78d29fd64d659c3.png&amp;r=x&amp;s=140" width="24" />
            <a href="/GrahamDennis">GrahamDennis</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Daniel Hahler" height="24" src="https://0.gravatar.com/avatar/abbc3c9698510a9c8af73f8b7bfacc1d?d=https%3A%2F%2Fidenticons.github.com%2F86636b6605b2bcb9a738d0e9bbce3c43.png&amp;r=x&amp;s=140" width="24" />
            <a href="/blueyed">blueyed</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Mika Laitio" height="24" src="https://2.gravatar.com/avatar/72c9d8b3bfbbe80bc98fe90d779adb0e?d=https%3A%2F%2Fidenticons.github.com%2Ffd9dadff4db66f0f1ddbc4c3b3852db1.png&amp;r=x&amp;s=140" width="24" />
            <a href="/lamikr">lamikr</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Erik Bray" height="24" src="https://2.gravatar.com/avatar/c7d341e2b002754f2b21fbab3a3fd072?d=https%3A%2F%2Fidenticons.github.com%2F672a2ceeecfb9bb3640e27afcada6124.png&amp;r=x&amp;s=140" width="24" />
            <a href="/embray">embray</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Neil Holley" height="24" src="https://0.gravatar.com/avatar/5fe1b081b534a5490fd7af2219de4cf2?d=https%3A%2F%2Fidenticons.github.com%2F536edb51ca8ae0417ec9ff4a66961ced.png&amp;r=x&amp;s=140" width="24" />
            <a href="/nholley">nholley</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Evan" height="24" src="https://0.gravatar.com/avatar/d73164d2180b4cf6099526e42e33a7fd?d=https%3A%2F%2Fidenticons.github.com%2F25e195ab826e7cd68a64c0a6673a1c8e.png&amp;r=x&amp;s=140" width="24" />
            <a href="/nightpool">nightpool</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Konstantin Zemlyak" height="24" src="https://0.gravatar.com/avatar/9b1d99a4017bdcfd438e1d433abcc8a4?d=https%3A%2F%2Fidenticons.github.com%2F22fccfd7e8a13a73e854da19e8f6e4fc.png&amp;r=x&amp;s=140" width="24" />
            <a href="/zart">zart</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Doug Hellmann" height="24" src="https://2.gravatar.com/avatar/4021eb3a9a363520e27c736cec6905e6?d=https%3A%2F%2Fidenticons.github.com%2F5ea8a1f62e96aa638379b4cdd5090013.png&amp;r=x&amp;s=140" width="24" />
            <a href="/dhellmann">dhellmann</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Jeremy Orem" height="24" src="https://1.gravatar.com/avatar/0abbaad38ae50fdaa8281e3ed39eabae?d=https%3A%2F%2Fidenticons.github.com%2Ff3a15bc2d3fd476dc91a56ea54b1baf9.png&amp;r=x&amp;s=140" width="24" />
            <a href="/oremj">oremj</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Daniel Holth" height="24" src="https://1.gravatar.com/avatar/087bc3a6b2fe0dbbf39ca49f40e2bac1?d=https%3A%2F%2Fidenticons.github.com%2F147b72ef22a54ce42cb0fd645c227c1b.png&amp;r=x&amp;s=140" width="24" />
            <a href="/dholth">dholth</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Preston Holmes" height="24" src="https://1.gravatar.com/avatar/d38343994d650e09acf2861e4b5db41a?d=https%3A%2F%2Fidenticons.github.com%2F0c24bb115003e07539daeb5370faf136.png&amp;r=x&amp;s=140" width="24" />
            <a href="/ptone">ptone</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Christos Kontas" height="24" src="https://0.gravatar.com/avatar/974436b9671794c9acb5233ac6719f78?d=https%3A%2F%2Fidenticons.github.com%2F56ca882239a4a41514328880afd6ac4f.png&amp;r=x&amp;s=140" width="24" />
            <a href="/xakon">xakon</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Dan Sully" height="24" src="https://0.gravatar.com/avatar/ee1cbfd6a5963de09d6109aa56e15632?d=https%3A%2F%2Fidenticons.github.com%2F3ac1fc4ea518c8f25ef3366bf240395a.png&amp;r=x&amp;s=140" width="24" />
            <a href="/dsully">dsully</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Damien Nozay" height="24" src="https://1.gravatar.com/avatar/5b886d4df174af783771e8a4dbaa4bf7?d=https%3A%2F%2Fidenticons.github.com%2F22fbb4e63fd70b05e64cf247e8305df2.png&amp;r=x&amp;s=140" width="24" />
            <a href="/dnozay">dnozay</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Ralf Schmitt" height="24" src="https://2.gravatar.com/avatar/1548e13088e0f8e55c25f4c543ad9140?d=https%3A%2F%2Fidenticons.github.com%2Fed5dbdd2da9881c10dc1a37f4472042f.png&amp;r=x&amp;s=140" width="24" />
            <a href="/schmir">schmir</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Chris McDonough" height="24" src="https://1.gravatar.com/avatar/a709fd00fc849280c23233ef0a01c5dc?d=https%3A%2F%2Fidenticons.github.com%2F7f988bf7cf75ed5449870dbc6edbfa2a.png&amp;r=x&amp;s=140" width="24" />
            <a href="/mcdonc">mcdonc</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Ronny Pfannschmidt" height="24" src="https://1.gravatar.com/avatar/4ab216eb1f5bdc9b9b2b7d855de1ef92?d=https%3A%2F%2Fidenticons.github.com%2F6dc9dde1649d6191fa1806e2b61195b9.png&amp;r=x&amp;s=140" width="24" />
            <a href="/RonnyPfannschmidt">RonnyPfannschmidt</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Thomas Aglassinger" height="24" src="https://0.gravatar.com/avatar/b58d0f1ea06b8d5de5f02c53f747ac03?d=https%3A%2F%2Fidenticons.github.com%2F2cc1fc711adeda72095f5246cee38675.png&amp;r=x&amp;s=140" width="24" />
            <a href="/roskakori">roskakori</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Satrajit Ghosh" height="24" src="https://2.gravatar.com/avatar/d3afc58453bc273dc015254e1d9581b3?d=https%3A%2F%2Fidenticons.github.com%2Fe16fd39f2bb95583b922e73afe6a0c5a.png&amp;r=x&amp;s=140" width="24" />
            <a href="/satra">satra</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Cap Petschulat" height="24" src="https://2.gravatar.com/avatar/a9401e2d1a0c784b9b8ba5dfbc49272f?d=https%3A%2F%2Fidenticons.github.com%2F242693e0e518a473d4374f84de433521.png&amp;r=x&amp;s=140" width="24" />
            <a href="/cap">cap</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Christian Stefanescu" height="24" src="https://2.gravatar.com/avatar/f6fc838795dde1f2ebf5b97cfb630142?d=https%3A%2F%2Fidenticons.github.com%2F87468f2b3ad403d5e91d48bc02a93d70.png&amp;r=x&amp;s=140" width="24" />
            <a href="/stchris">stchris</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Bradley Ayers" height="24" src="https://2.gravatar.com/avatar/9515ab087a2ca71270e6844366f6e689?d=https%3A%2F%2Fidenticons.github.com%2F3ed3287eb3a47bbf2e1d00ae3c45ec22.png&amp;r=x&amp;s=140" width="24" />
            <a href="/bradleyayers">bradleyayers</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Min RK" height="24" src="https://1.gravatar.com/avatar/d5b897c37001627c2e3ad3c1e8a7e6fb?d=https%3A%2F%2Fidenticons.github.com%2Ffd0c473f5aa5802a4e75f406e992c687.png&amp;r=x&amp;s=140" width="24" />
            <a href="/minrk">minrk</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="anatoly techtonik" height="24" src="https://0.gravatar.com/avatar/9d7e611f31c52f4d62bbe279d4f334de?d=https%3A%2F%2Fidenticons.github.com%2F38ce7082d6b529e9be9a0c65c6a38528.png&amp;r=x&amp;s=140" width="24" />
            <a href="/techtonik">techtonik</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Brian Kearns" height="24" src="https://0.gravatar.com/avatar/87f7ab861840a40e86ff91a7c18c7884?d=https%3A%2F%2Fidenticons.github.com%2Ff573ea37d4684de6a515c13aa0341ac4.png&amp;r=x&amp;s=140" width="24" />
            <a href="/bdkearns">bdkearns</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Vinay Sajip" height="24" src="https://1.gravatar.com/avatar/7094252405dd3dd5f798b132834d39b2?d=https%3A%2F%2Fidenticons.github.com%2F145256db875d146462171766f68588e3.png&amp;r=x&amp;s=140" width="24" />
            <a href="/vsajip">vsajip</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Vladimir Dmitriev" height="24" src="https://1.gravatar.com/avatar/8efdc74d30fe5b0ea49fc91ba682f0bc?d=https%3A%2F%2Fidenticons.github.com%2F3f5df31d33d5e575b6f733e2c6a2db42.png&amp;r=x&amp;s=140" width="24" />
            <a href="/vldmit">vldmit</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Armin Ronacher" height="24" src="https://0.gravatar.com/avatar/181de1fb11dffe39774f3e2e23cda3b6?d=https%3A%2F%2Fidenticons.github.com%2F8606f35ec6c77858dfb80a385d0d1151.png&amp;r=x&amp;s=140" width="24" />
            <a href="/mitsuhiko">mitsuhiko</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Douglas Creager" height="24" src="https://0.gravatar.com/avatar/04ee3ca11f1ae11c63faa7995dbf1ed7?d=https%3A%2F%2Fidenticons.github.com%2F7a2b33c672ce223b2aa5789171ddde2f.png&amp;r=x&amp;s=140" width="24" />
            <a href="/dcreager">dcreager</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Doug Napoleone" height="24" src="https://1.gravatar.com/avatar/336cb13a0e2ae8c919e4dec96a43cb0e?d=https%3A%2F%2Fidenticons.github.com%2Fefb9833652b01e4834fd4226292f97b7.png&amp;r=x&amp;s=140" width="24" />
            <a href="/dougn">dougn</a>
          </li>
      </ul>
    </div>
  </div>

<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">executable file</span>
          <span>2337 lines (2126 sloc)</span>
        <span>98.341 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton disabled tooltipped leftwards" href="#"
                 title="You must be signed in to make or propose changes">Edit</a>
          <a href="/pypa/virtualenv/raw/develop/virtualenv.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/pypa/virtualenv/blame/develop/virtualenv.py" class="button minibutton js-update-url-with-hash">Blame</a>
          <a href="/pypa/virtualenv/commits/develop/virtualenv.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger disabled empty-icon tooltipped leftwards" href="#"
             title="You must be signed in to make or propose changes">
          Delete
        </a>
      </div><!-- /.actions -->
    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff tab-size-8">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>
<span id="L441" rel="#L441">441</span>
<span id="L442" rel="#L442">442</span>
<span id="L443" rel="#L443">443</span>
<span id="L444" rel="#L444">444</span>
<span id="L445" rel="#L445">445</span>
<span id="L446" rel="#L446">446</span>
<span id="L447" rel="#L447">447</span>
<span id="L448" rel="#L448">448</span>
<span id="L449" rel="#L449">449</span>
<span id="L450" rel="#L450">450</span>
<span id="L451" rel="#L451">451</span>
<span id="L452" rel="#L452">452</span>
<span id="L453" rel="#L453">453</span>
<span id="L454" rel="#L454">454</span>
<span id="L455" rel="#L455">455</span>
<span id="L456" rel="#L456">456</span>
<span id="L457" rel="#L457">457</span>
<span id="L458" rel="#L458">458</span>
<span id="L459" rel="#L459">459</span>
<span id="L460" rel="#L460">460</span>
<span id="L461" rel="#L461">461</span>
<span id="L462" rel="#L462">462</span>
<span id="L463" rel="#L463">463</span>
<span id="L464" rel="#L464">464</span>
<span id="L465" rel="#L465">465</span>
<span id="L466" rel="#L466">466</span>
<span id="L467" rel="#L467">467</span>
<span id="L468" rel="#L468">468</span>
<span id="L469" rel="#L469">469</span>
<span id="L470" rel="#L470">470</span>
<span id="L471" rel="#L471">471</span>
<span id="L472" rel="#L472">472</span>
<span id="L473" rel="#L473">473</span>
<span id="L474" rel="#L474">474</span>
<span id="L475" rel="#L475">475</span>
<span id="L476" rel="#L476">476</span>
<span id="L477" rel="#L477">477</span>
<span id="L478" rel="#L478">478</span>
<span id="L479" rel="#L479">479</span>
<span id="L480" rel="#L480">480</span>
<span id="L481" rel="#L481">481</span>
<span id="L482" rel="#L482">482</span>
<span id="L483" rel="#L483">483</span>
<span id="L484" rel="#L484">484</span>
<span id="L485" rel="#L485">485</span>
<span id="L486" rel="#L486">486</span>
<span id="L487" rel="#L487">487</span>
<span id="L488" rel="#L488">488</span>
<span id="L489" rel="#L489">489</span>
<span id="L490" rel="#L490">490</span>
<span id="L491" rel="#L491">491</span>
<span id="L492" rel="#L492">492</span>
<span id="L493" rel="#L493">493</span>
<span id="L494" rel="#L494">494</span>
<span id="L495" rel="#L495">495</span>
<span id="L496" rel="#L496">496</span>
<span id="L497" rel="#L497">497</span>
<span id="L498" rel="#L498">498</span>
<span id="L499" rel="#L499">499</span>
<span id="L500" rel="#L500">500</span>
<span id="L501" rel="#L501">501</span>
<span id="L502" rel="#L502">502</span>
<span id="L503" rel="#L503">503</span>
<span id="L504" rel="#L504">504</span>
<span id="L505" rel="#L505">505</span>
<span id="L506" rel="#L506">506</span>
<span id="L507" rel="#L507">507</span>
<span id="L508" rel="#L508">508</span>
<span id="L509" rel="#L509">509</span>
<span id="L510" rel="#L510">510</span>
<span id="L511" rel="#L511">511</span>
<span id="L512" rel="#L512">512</span>
<span id="L513" rel="#L513">513</span>
<span id="L514" rel="#L514">514</span>
<span id="L515" rel="#L515">515</span>
<span id="L516" rel="#L516">516</span>
<span id="L517" rel="#L517">517</span>
<span id="L518" rel="#L518">518</span>
<span id="L519" rel="#L519">519</span>
<span id="L520" rel="#L520">520</span>
<span id="L521" rel="#L521">521</span>
<span id="L522" rel="#L522">522</span>
<span id="L523" rel="#L523">523</span>
<span id="L524" rel="#L524">524</span>
<span id="L525" rel="#L525">525</span>
<span id="L526" rel="#L526">526</span>
<span id="L527" rel="#L527">527</span>
<span id="L528" rel="#L528">528</span>
<span id="L529" rel="#L529">529</span>
<span id="L530" rel="#L530">530</span>
<span id="L531" rel="#L531">531</span>
<span id="L532" rel="#L532">532</span>
<span id="L533" rel="#L533">533</span>
<span id="L534" rel="#L534">534</span>
<span id="L535" rel="#L535">535</span>
<span id="L536" rel="#L536">536</span>
<span id="L537" rel="#L537">537</span>
<span id="L538" rel="#L538">538</span>
<span id="L539" rel="#L539">539</span>
<span id="L540" rel="#L540">540</span>
<span id="L541" rel="#L541">541</span>
<span id="L542" rel="#L542">542</span>
<span id="L543" rel="#L543">543</span>
<span id="L544" rel="#L544">544</span>
<span id="L545" rel="#L545">545</span>
<span id="L546" rel="#L546">546</span>
<span id="L547" rel="#L547">547</span>
<span id="L548" rel="#L548">548</span>
<span id="L549" rel="#L549">549</span>
<span id="L550" rel="#L550">550</span>
<span id="L551" rel="#L551">551</span>
<span id="L552" rel="#L552">552</span>
<span id="L553" rel="#L553">553</span>
<span id="L554" rel="#L554">554</span>
<span id="L555" rel="#L555">555</span>
<span id="L556" rel="#L556">556</span>
<span id="L557" rel="#L557">557</span>
<span id="L558" rel="#L558">558</span>
<span id="L559" rel="#L559">559</span>
<span id="L560" rel="#L560">560</span>
<span id="L561" rel="#L561">561</span>
<span id="L562" rel="#L562">562</span>
<span id="L563" rel="#L563">563</span>
<span id="L564" rel="#L564">564</span>
<span id="L565" rel="#L565">565</span>
<span id="L566" rel="#L566">566</span>
<span id="L567" rel="#L567">567</span>
<span id="L568" rel="#L568">568</span>
<span id="L569" rel="#L569">569</span>
<span id="L570" rel="#L570">570</span>
<span id="L571" rel="#L571">571</span>
<span id="L572" rel="#L572">572</span>
<span id="L573" rel="#L573">573</span>
<span id="L574" rel="#L574">574</span>
<span id="L575" rel="#L575">575</span>
<span id="L576" rel="#L576">576</span>
<span id="L577" rel="#L577">577</span>
<span id="L578" rel="#L578">578</span>
<span id="L579" rel="#L579">579</span>
<span id="L580" rel="#L580">580</span>
<span id="L581" rel="#L581">581</span>
<span id="L582" rel="#L582">582</span>
<span id="L583" rel="#L583">583</span>
<span id="L584" rel="#L584">584</span>
<span id="L585" rel="#L585">585</span>
<span id="L586" rel="#L586">586</span>
<span id="L587" rel="#L587">587</span>
<span id="L588" rel="#L588">588</span>
<span id="L589" rel="#L589">589</span>
<span id="L590" rel="#L590">590</span>
<span id="L591" rel="#L591">591</span>
<span id="L592" rel="#L592">592</span>
<span id="L593" rel="#L593">593</span>
<span id="L594" rel="#L594">594</span>
<span id="L595" rel="#L595">595</span>
<span id="L596" rel="#L596">596</span>
<span id="L597" rel="#L597">597</span>
<span id="L598" rel="#L598">598</span>
<span id="L599" rel="#L599">599</span>
<span id="L600" rel="#L600">600</span>
<span id="L601" rel="#L601">601</span>
<span id="L602" rel="#L602">602</span>
<span id="L603" rel="#L603">603</span>
<span id="L604" rel="#L604">604</span>
<span id="L605" rel="#L605">605</span>
<span id="L606" rel="#L606">606</span>
<span id="L607" rel="#L607">607</span>
<span id="L608" rel="#L608">608</span>
<span id="L609" rel="#L609">609</span>
<span id="L610" rel="#L610">610</span>
<span id="L611" rel="#L611">611</span>
<span id="L612" rel="#L612">612</span>
<span id="L613" rel="#L613">613</span>
<span id="L614" rel="#L614">614</span>
<span id="L615" rel="#L615">615</span>
<span id="L616" rel="#L616">616</span>
<span id="L617" rel="#L617">617</span>
<span id="L618" rel="#L618">618</span>
<span id="L619" rel="#L619">619</span>
<span id="L620" rel="#L620">620</span>
<span id="L621" rel="#L621">621</span>
<span id="L622" rel="#L622">622</span>
<span id="L623" rel="#L623">623</span>
<span id="L624" rel="#L624">624</span>
<span id="L625" rel="#L625">625</span>
<span id="L626" rel="#L626">626</span>
<span id="L627" rel="#L627">627</span>
<span id="L628" rel="#L628">628</span>
<span id="L629" rel="#L629">629</span>
<span id="L630" rel="#L630">630</span>
<span id="L631" rel="#L631">631</span>
<span id="L632" rel="#L632">632</span>
<span id="L633" rel="#L633">633</span>
<span id="L634" rel="#L634">634</span>
<span id="L635" rel="#L635">635</span>
<span id="L636" rel="#L636">636</span>
<span id="L637" rel="#L637">637</span>
<span id="L638" rel="#L638">638</span>
<span id="L639" rel="#L639">639</span>
<span id="L640" rel="#L640">640</span>
<span id="L641" rel="#L641">641</span>
<span id="L642" rel="#L642">642</span>
<span id="L643" rel="#L643">643</span>
<span id="L644" rel="#L644">644</span>
<span id="L645" rel="#L645">645</span>
<span id="L646" rel="#L646">646</span>
<span id="L647" rel="#L647">647</span>
<span id="L648" rel="#L648">648</span>
<span id="L649" rel="#L649">649</span>
<span id="L650" rel="#L650">650</span>
<span id="L651" rel="#L651">651</span>
<span id="L652" rel="#L652">652</span>
<span id="L653" rel="#L653">653</span>
<span id="L654" rel="#L654">654</span>
<span id="L655" rel="#L655">655</span>
<span id="L656" rel="#L656">656</span>
<span id="L657" rel="#L657">657</span>
<span id="L658" rel="#L658">658</span>
<span id="L659" rel="#L659">659</span>
<span id="L660" rel="#L660">660</span>
<span id="L661" rel="#L661">661</span>
<span id="L662" rel="#L662">662</span>
<span id="L663" rel="#L663">663</span>
<span id="L664" rel="#L664">664</span>
<span id="L665" rel="#L665">665</span>
<span id="L666" rel="#L666">666</span>
<span id="L667" rel="#L667">667</span>
<span id="L668" rel="#L668">668</span>
<span id="L669" rel="#L669">669</span>
<span id="L670" rel="#L670">670</span>
<span id="L671" rel="#L671">671</span>
<span id="L672" rel="#L672">672</span>
<span id="L673" rel="#L673">673</span>
<span id="L674" rel="#L674">674</span>
<span id="L675" rel="#L675">675</span>
<span id="L676" rel="#L676">676</span>
<span id="L677" rel="#L677">677</span>
<span id="L678" rel="#L678">678</span>
<span id="L679" rel="#L679">679</span>
<span id="L680" rel="#L680">680</span>
<span id="L681" rel="#L681">681</span>
<span id="L682" rel="#L682">682</span>
<span id="L683" rel="#L683">683</span>
<span id="L684" rel="#L684">684</span>
<span id="L685" rel="#L685">685</span>
<span id="L686" rel="#L686">686</span>
<span id="L687" rel="#L687">687</span>
<span id="L688" rel="#L688">688</span>
<span id="L689" rel="#L689">689</span>
<span id="L690" rel="#L690">690</span>
<span id="L691" rel="#L691">691</span>
<span id="L692" rel="#L692">692</span>
<span id="L693" rel="#L693">693</span>
<span id="L694" rel="#L694">694</span>
<span id="L695" rel="#L695">695</span>
<span id="L696" rel="#L696">696</span>
<span id="L697" rel="#L697">697</span>
<span id="L698" rel="#L698">698</span>
<span id="L699" rel="#L699">699</span>
<span id="L700" rel="#L700">700</span>
<span id="L701" rel="#L701">701</span>
<span id="L702" rel="#L702">702</span>
<span id="L703" rel="#L703">703</span>
<span id="L704" rel="#L704">704</span>
<span id="L705" rel="#L705">705</span>
<span id="L706" rel="#L706">706</span>
<span id="L707" rel="#L707">707</span>
<span id="L708" rel="#L708">708</span>
<span id="L709" rel="#L709">709</span>
<span id="L710" rel="#L710">710</span>
<span id="L711" rel="#L711">711</span>
<span id="L712" rel="#L712">712</span>
<span id="L713" rel="#L713">713</span>
<span id="L714" rel="#L714">714</span>
<span id="L715" rel="#L715">715</span>
<span id="L716" rel="#L716">716</span>
<span id="L717" rel="#L717">717</span>
<span id="L718" rel="#L718">718</span>
<span id="L719" rel="#L719">719</span>
<span id="L720" rel="#L720">720</span>
<span id="L721" rel="#L721">721</span>
<span id="L722" rel="#L722">722</span>
<span id="L723" rel="#L723">723</span>
<span id="L724" rel="#L724">724</span>
<span id="L725" rel="#L725">725</span>
<span id="L726" rel="#L726">726</span>
<span id="L727" rel="#L727">727</span>
<span id="L728" rel="#L728">728</span>
<span id="L729" rel="#L729">729</span>
<span id="L730" rel="#L730">730</span>
<span id="L731" rel="#L731">731</span>
<span id="L732" rel="#L732">732</span>
<span id="L733" rel="#L733">733</span>
<span id="L734" rel="#L734">734</span>
<span id="L735" rel="#L735">735</span>
<span id="L736" rel="#L736">736</span>
<span id="L737" rel="#L737">737</span>
<span id="L738" rel="#L738">738</span>
<span id="L739" rel="#L739">739</span>
<span id="L740" rel="#L740">740</span>
<span id="L741" rel="#L741">741</span>
<span id="L742" rel="#L742">742</span>
<span id="L743" rel="#L743">743</span>
<span id="L744" rel="#L744">744</span>
<span id="L745" rel="#L745">745</span>
<span id="L746" rel="#L746">746</span>
<span id="L747" rel="#L747">747</span>
<span id="L748" rel="#L748">748</span>
<span id="L749" rel="#L749">749</span>
<span id="L750" rel="#L750">750</span>
<span id="L751" rel="#L751">751</span>
<span id="L752" rel="#L752">752</span>
<span id="L753" rel="#L753">753</span>
<span id="L754" rel="#L754">754</span>
<span id="L755" rel="#L755">755</span>
<span id="L756" rel="#L756">756</span>
<span id="L757" rel="#L757">757</span>
<span id="L758" rel="#L758">758</span>
<span id="L759" rel="#L759">759</span>
<span id="L760" rel="#L760">760</span>
<span id="L761" rel="#L761">761</span>
<span id="L762" rel="#L762">762</span>
<span id="L763" rel="#L763">763</span>
<span id="L764" rel="#L764">764</span>
<span id="L765" rel="#L765">765</span>
<span id="L766" rel="#L766">766</span>
<span id="L767" rel="#L767">767</span>
<span id="L768" rel="#L768">768</span>
<span id="L769" rel="#L769">769</span>
<span id="L770" rel="#L770">770</span>
<span id="L771" rel="#L771">771</span>
<span id="L772" rel="#L772">772</span>
<span id="L773" rel="#L773">773</span>
<span id="L774" rel="#L774">774</span>
<span id="L775" rel="#L775">775</span>
<span id="L776" rel="#L776">776</span>
<span id="L777" rel="#L777">777</span>
<span id="L778" rel="#L778">778</span>
<span id="L779" rel="#L779">779</span>
<span id="L780" rel="#L780">780</span>
<span id="L781" rel="#L781">781</span>
<span id="L782" rel="#L782">782</span>
<span id="L783" rel="#L783">783</span>
<span id="L784" rel="#L784">784</span>
<span id="L785" rel="#L785">785</span>
<span id="L786" rel="#L786">786</span>
<span id="L787" rel="#L787">787</span>
<span id="L788" rel="#L788">788</span>
<span id="L789" rel="#L789">789</span>
<span id="L790" rel="#L790">790</span>
<span id="L791" rel="#L791">791</span>
<span id="L792" rel="#L792">792</span>
<span id="L793" rel="#L793">793</span>
<span id="L794" rel="#L794">794</span>
<span id="L795" rel="#L795">795</span>
<span id="L796" rel="#L796">796</span>
<span id="L797" rel="#L797">797</span>
<span id="L798" rel="#L798">798</span>
<span id="L799" rel="#L799">799</span>
<span id="L800" rel="#L800">800</span>
<span id="L801" rel="#L801">801</span>
<span id="L802" rel="#L802">802</span>
<span id="L803" rel="#L803">803</span>
<span id="L804" rel="#L804">804</span>
<span id="L805" rel="#L805">805</span>
<span id="L806" rel="#L806">806</span>
<span id="L807" rel="#L807">807</span>
<span id="L808" rel="#L808">808</span>
<span id="L809" rel="#L809">809</span>
<span id="L810" rel="#L810">810</span>
<span id="L811" rel="#L811">811</span>
<span id="L812" rel="#L812">812</span>
<span id="L813" rel="#L813">813</span>
<span id="L814" rel="#L814">814</span>
<span id="L815" rel="#L815">815</span>
<span id="L816" rel="#L816">816</span>
<span id="L817" rel="#L817">817</span>
<span id="L818" rel="#L818">818</span>
<span id="L819" rel="#L819">819</span>
<span id="L820" rel="#L820">820</span>
<span id="L821" rel="#L821">821</span>
<span id="L822" rel="#L822">822</span>
<span id="L823" rel="#L823">823</span>
<span id="L824" rel="#L824">824</span>
<span id="L825" rel="#L825">825</span>
<span id="L826" rel="#L826">826</span>
<span id="L827" rel="#L827">827</span>
<span id="L828" rel="#L828">828</span>
<span id="L829" rel="#L829">829</span>
<span id="L830" rel="#L830">830</span>
<span id="L831" rel="#L831">831</span>
<span id="L832" rel="#L832">832</span>
<span id="L833" rel="#L833">833</span>
<span id="L834" rel="#L834">834</span>
<span id="L835" rel="#L835">835</span>
<span id="L836" rel="#L836">836</span>
<span id="L837" rel="#L837">837</span>
<span id="L838" rel="#L838">838</span>
<span id="L839" rel="#L839">839</span>
<span id="L840" rel="#L840">840</span>
<span id="L841" rel="#L841">841</span>
<span id="L842" rel="#L842">842</span>
<span id="L843" rel="#L843">843</span>
<span id="L844" rel="#L844">844</span>
<span id="L845" rel="#L845">845</span>
<span id="L846" rel="#L846">846</span>
<span id="L847" rel="#L847">847</span>
<span id="L848" rel="#L848">848</span>
<span id="L849" rel="#L849">849</span>
<span id="L850" rel="#L850">850</span>
<span id="L851" rel="#L851">851</span>
<span id="L852" rel="#L852">852</span>
<span id="L853" rel="#L853">853</span>
<span id="L854" rel="#L854">854</span>
<span id="L855" rel="#L855">855</span>
<span id="L856" rel="#L856">856</span>
<span id="L857" rel="#L857">857</span>
<span id="L858" rel="#L858">858</span>
<span id="L859" rel="#L859">859</span>
<span id="L860" rel="#L860">860</span>
<span id="L861" rel="#L861">861</span>
<span id="L862" rel="#L862">862</span>
<span id="L863" rel="#L863">863</span>
<span id="L864" rel="#L864">864</span>
<span id="L865" rel="#L865">865</span>
<span id="L866" rel="#L866">866</span>
<span id="L867" rel="#L867">867</span>
<span id="L868" rel="#L868">868</span>
<span id="L869" rel="#L869">869</span>
<span id="L870" rel="#L870">870</span>
<span id="L871" rel="#L871">871</span>
<span id="L872" rel="#L872">872</span>
<span id="L873" rel="#L873">873</span>
<span id="L874" rel="#L874">874</span>
<span id="L875" rel="#L875">875</span>
<span id="L876" rel="#L876">876</span>
<span id="L877" rel="#L877">877</span>
<span id="L878" rel="#L878">878</span>
<span id="L879" rel="#L879">879</span>
<span id="L880" rel="#L880">880</span>
<span id="L881" rel="#L881">881</span>
<span id="L882" rel="#L882">882</span>
<span id="L883" rel="#L883">883</span>
<span id="L884" rel="#L884">884</span>
<span id="L885" rel="#L885">885</span>
<span id="L886" rel="#L886">886</span>
<span id="L887" rel="#L887">887</span>
<span id="L888" rel="#L888">888</span>
<span id="L889" rel="#L889">889</span>
<span id="L890" rel="#L890">890</span>
<span id="L891" rel="#L891">891</span>
<span id="L892" rel="#L892">892</span>
<span id="L893" rel="#L893">893</span>
<span id="L894" rel="#L894">894</span>
<span id="L895" rel="#L895">895</span>
<span id="L896" rel="#L896">896</span>
<span id="L897" rel="#L897">897</span>
<span id="L898" rel="#L898">898</span>
<span id="L899" rel="#L899">899</span>
<span id="L900" rel="#L900">900</span>
<span id="L901" rel="#L901">901</span>
<span id="L902" rel="#L902">902</span>
<span id="L903" rel="#L903">903</span>
<span id="L904" rel="#L904">904</span>
<span id="L905" rel="#L905">905</span>
<span id="L906" rel="#L906">906</span>
<span id="L907" rel="#L907">907</span>
<span id="L908" rel="#L908">908</span>
<span id="L909" rel="#L909">909</span>
<span id="L910" rel="#L910">910</span>
<span id="L911" rel="#L911">911</span>
<span id="L912" rel="#L912">912</span>
<span id="L913" rel="#L913">913</span>
<span id="L914" rel="#L914">914</span>
<span id="L915" rel="#L915">915</span>
<span id="L916" rel="#L916">916</span>
<span id="L917" rel="#L917">917</span>
<span id="L918" rel="#L918">918</span>
<span id="L919" rel="#L919">919</span>
<span id="L920" rel="#L920">920</span>
<span id="L921" rel="#L921">921</span>
<span id="L922" rel="#L922">922</span>
<span id="L923" rel="#L923">923</span>
<span id="L924" rel="#L924">924</span>
<span id="L925" rel="#L925">925</span>
<span id="L926" rel="#L926">926</span>
<span id="L927" rel="#L927">927</span>
<span id="L928" rel="#L928">928</span>
<span id="L929" rel="#L929">929</span>
<span id="L930" rel="#L930">930</span>
<span id="L931" rel="#L931">931</span>
<span id="L932" rel="#L932">932</span>
<span id="L933" rel="#L933">933</span>
<span id="L934" rel="#L934">934</span>
<span id="L935" rel="#L935">935</span>
<span id="L936" rel="#L936">936</span>
<span id="L937" rel="#L937">937</span>
<span id="L938" rel="#L938">938</span>
<span id="L939" rel="#L939">939</span>
<span id="L940" rel="#L940">940</span>
<span id="L941" rel="#L941">941</span>
<span id="L942" rel="#L942">942</span>
<span id="L943" rel="#L943">943</span>
<span id="L944" rel="#L944">944</span>
<span id="L945" rel="#L945">945</span>
<span id="L946" rel="#L946">946</span>
<span id="L947" rel="#L947">947</span>
<span id="L948" rel="#L948">948</span>
<span id="L949" rel="#L949">949</span>
<span id="L950" rel="#L950">950</span>
<span id="L951" rel="#L951">951</span>
<span id="L952" rel="#L952">952</span>
<span id="L953" rel="#L953">953</span>
<span id="L954" rel="#L954">954</span>
<span id="L955" rel="#L955">955</span>
<span id="L956" rel="#L956">956</span>
<span id="L957" rel="#L957">957</span>
<span id="L958" rel="#L958">958</span>
<span id="L959" rel="#L959">959</span>
<span id="L960" rel="#L960">960</span>
<span id="L961" rel="#L961">961</span>
<span id="L962" rel="#L962">962</span>
<span id="L963" rel="#L963">963</span>
<span id="L964" rel="#L964">964</span>
<span id="L965" rel="#L965">965</span>
<span id="L966" rel="#L966">966</span>
<span id="L967" rel="#L967">967</span>
<span id="L968" rel="#L968">968</span>
<span id="L969" rel="#L969">969</span>
<span id="L970" rel="#L970">970</span>
<span id="L971" rel="#L971">971</span>
<span id="L972" rel="#L972">972</span>
<span id="L973" rel="#L973">973</span>
<span id="L974" rel="#L974">974</span>
<span id="L975" rel="#L975">975</span>
<span id="L976" rel="#L976">976</span>
<span id="L977" rel="#L977">977</span>
<span id="L978" rel="#L978">978</span>
<span id="L979" rel="#L979">979</span>
<span id="L980" rel="#L980">980</span>
<span id="L981" rel="#L981">981</span>
<span id="L982" rel="#L982">982</span>
<span id="L983" rel="#L983">983</span>
<span id="L984" rel="#L984">984</span>
<span id="L985" rel="#L985">985</span>
<span id="L986" rel="#L986">986</span>
<span id="L987" rel="#L987">987</span>
<span id="L988" rel="#L988">988</span>
<span id="L989" rel="#L989">989</span>
<span id="L990" rel="#L990">990</span>
<span id="L991" rel="#L991">991</span>
<span id="L992" rel="#L992">992</span>
<span id="L993" rel="#L993">993</span>
<span id="L994" rel="#L994">994</span>
<span id="L995" rel="#L995">995</span>
<span id="L996" rel="#L996">996</span>
<span id="L997" rel="#L997">997</span>
<span id="L998" rel="#L998">998</span>
<span id="L999" rel="#L999">999</span>
<span id="L1000" rel="#L1000">1000</span>
<span id="L1001" rel="#L1001">1001</span>
<span id="L1002" rel="#L1002">1002</span>
<span id="L1003" rel="#L1003">1003</span>
<span id="L1004" rel="#L1004">1004</span>
<span id="L1005" rel="#L1005">1005</span>
<span id="L1006" rel="#L1006">1006</span>
<span id="L1007" rel="#L1007">1007</span>
<span id="L1008" rel="#L1008">1008</span>
<span id="L1009" rel="#L1009">1009</span>
<span id="L1010" rel="#L1010">1010</span>
<span id="L1011" rel="#L1011">1011</span>
<span id="L1012" rel="#L1012">1012</span>
<span id="L1013" rel="#L1013">1013</span>
<span id="L1014" rel="#L1014">1014</span>
<span id="L1015" rel="#L1015">1015</span>
<span id="L1016" rel="#L1016">1016</span>
<span id="L1017" rel="#L1017">1017</span>
<span id="L1018" rel="#L1018">1018</span>
<span id="L1019" rel="#L1019">1019</span>
<span id="L1020" rel="#L1020">1020</span>
<span id="L1021" rel="#L1021">1021</span>
<span id="L1022" rel="#L1022">1022</span>
<span id="L1023" rel="#L1023">1023</span>
<span id="L1024" rel="#L1024">1024</span>
<span id="L1025" rel="#L1025">1025</span>
<span id="L1026" rel="#L1026">1026</span>
<span id="L1027" rel="#L1027">1027</span>
<span id="L1028" rel="#L1028">1028</span>
<span id="L1029" rel="#L1029">1029</span>
<span id="L1030" rel="#L1030">1030</span>
<span id="L1031" rel="#L1031">1031</span>
<span id="L1032" rel="#L1032">1032</span>
<span id="L1033" rel="#L1033">1033</span>
<span id="L1034" rel="#L1034">1034</span>
<span id="L1035" rel="#L1035">1035</span>
<span id="L1036" rel="#L1036">1036</span>
<span id="L1037" rel="#L1037">1037</span>
<span id="L1038" rel="#L1038">1038</span>
<span id="L1039" rel="#L1039">1039</span>
<span id="L1040" rel="#L1040">1040</span>
<span id="L1041" rel="#L1041">1041</span>
<span id="L1042" rel="#L1042">1042</span>
<span id="L1043" rel="#L1043">1043</span>
<span id="L1044" rel="#L1044">1044</span>
<span id="L1045" rel="#L1045">1045</span>
<span id="L1046" rel="#L1046">1046</span>
<span id="L1047" rel="#L1047">1047</span>
<span id="L1048" rel="#L1048">1048</span>
<span id="L1049" rel="#L1049">1049</span>
<span id="L1050" rel="#L1050">1050</span>
<span id="L1051" rel="#L1051">1051</span>
<span id="L1052" rel="#L1052">1052</span>
<span id="L1053" rel="#L1053">1053</span>
<span id="L1054" rel="#L1054">1054</span>
<span id="L1055" rel="#L1055">1055</span>
<span id="L1056" rel="#L1056">1056</span>
<span id="L1057" rel="#L1057">1057</span>
<span id="L1058" rel="#L1058">1058</span>
<span id="L1059" rel="#L1059">1059</span>
<span id="L1060" rel="#L1060">1060</span>
<span id="L1061" rel="#L1061">1061</span>
<span id="L1062" rel="#L1062">1062</span>
<span id="L1063" rel="#L1063">1063</span>
<span id="L1064" rel="#L1064">1064</span>
<span id="L1065" rel="#L1065">1065</span>
<span id="L1066" rel="#L1066">1066</span>
<span id="L1067" rel="#L1067">1067</span>
<span id="L1068" rel="#L1068">1068</span>
<span id="L1069" rel="#L1069">1069</span>
<span id="L1070" rel="#L1070">1070</span>
<span id="L1071" rel="#L1071">1071</span>
<span id="L1072" rel="#L1072">1072</span>
<span id="L1073" rel="#L1073">1073</span>
<span id="L1074" rel="#L1074">1074</span>
<span id="L1075" rel="#L1075">1075</span>
<span id="L1076" rel="#L1076">1076</span>
<span id="L1077" rel="#L1077">1077</span>
<span id="L1078" rel="#L1078">1078</span>
<span id="L1079" rel="#L1079">1079</span>
<span id="L1080" rel="#L1080">1080</span>
<span id="L1081" rel="#L1081">1081</span>
<span id="L1082" rel="#L1082">1082</span>
<span id="L1083" rel="#L1083">1083</span>
<span id="L1084" rel="#L1084">1084</span>
<span id="L1085" rel="#L1085">1085</span>
<span id="L1086" rel="#L1086">1086</span>
<span id="L1087" rel="#L1087">1087</span>
<span id="L1088" rel="#L1088">1088</span>
<span id="L1089" rel="#L1089">1089</span>
<span id="L1090" rel="#L1090">1090</span>
<span id="L1091" rel="#L1091">1091</span>
<span id="L1092" rel="#L1092">1092</span>
<span id="L1093" rel="#L1093">1093</span>
<span id="L1094" rel="#L1094">1094</span>
<span id="L1095" rel="#L1095">1095</span>
<span id="L1096" rel="#L1096">1096</span>
<span id="L1097" rel="#L1097">1097</span>
<span id="L1098" rel="#L1098">1098</span>
<span id="L1099" rel="#L1099">1099</span>
<span id="L1100" rel="#L1100">1100</span>
<span id="L1101" rel="#L1101">1101</span>
<span id="L1102" rel="#L1102">1102</span>
<span id="L1103" rel="#L1103">1103</span>
<span id="L1104" rel="#L1104">1104</span>
<span id="L1105" rel="#L1105">1105</span>
<span id="L1106" rel="#L1106">1106</span>
<span id="L1107" rel="#L1107">1107</span>
<span id="L1108" rel="#L1108">1108</span>
<span id="L1109" rel="#L1109">1109</span>
<span id="L1110" rel="#L1110">1110</span>
<span id="L1111" rel="#L1111">1111</span>
<span id="L1112" rel="#L1112">1112</span>
<span id="L1113" rel="#L1113">1113</span>
<span id="L1114" rel="#L1114">1114</span>
<span id="L1115" rel="#L1115">1115</span>
<span id="L1116" rel="#L1116">1116</span>
<span id="L1117" rel="#L1117">1117</span>
<span id="L1118" rel="#L1118">1118</span>
<span id="L1119" rel="#L1119">1119</span>
<span id="L1120" rel="#L1120">1120</span>
<span id="L1121" rel="#L1121">1121</span>
<span id="L1122" rel="#L1122">1122</span>
<span id="L1123" rel="#L1123">1123</span>
<span id="L1124" rel="#L1124">1124</span>
<span id="L1125" rel="#L1125">1125</span>
<span id="L1126" rel="#L1126">1126</span>
<span id="L1127" rel="#L1127">1127</span>
<span id="L1128" rel="#L1128">1128</span>
<span id="L1129" rel="#L1129">1129</span>
<span id="L1130" rel="#L1130">1130</span>
<span id="L1131" rel="#L1131">1131</span>
<span id="L1132" rel="#L1132">1132</span>
<span id="L1133" rel="#L1133">1133</span>
<span id="L1134" rel="#L1134">1134</span>
<span id="L1135" rel="#L1135">1135</span>
<span id="L1136" rel="#L1136">1136</span>
<span id="L1137" rel="#L1137">1137</span>
<span id="L1138" rel="#L1138">1138</span>
<span id="L1139" rel="#L1139">1139</span>
<span id="L1140" rel="#L1140">1140</span>
<span id="L1141" rel="#L1141">1141</span>
<span id="L1142" rel="#L1142">1142</span>
<span id="L1143" rel="#L1143">1143</span>
<span id="L1144" rel="#L1144">1144</span>
<span id="L1145" rel="#L1145">1145</span>
<span id="L1146" rel="#L1146">1146</span>
<span id="L1147" rel="#L1147">1147</span>
<span id="L1148" rel="#L1148">1148</span>
<span id="L1149" rel="#L1149">1149</span>
<span id="L1150" rel="#L1150">1150</span>
<span id="L1151" rel="#L1151">1151</span>
<span id="L1152" rel="#L1152">1152</span>
<span id="L1153" rel="#L1153">1153</span>
<span id="L1154" rel="#L1154">1154</span>
<span id="L1155" rel="#L1155">1155</span>
<span id="L1156" rel="#L1156">1156</span>
<span id="L1157" rel="#L1157">1157</span>
<span id="L1158" rel="#L1158">1158</span>
<span id="L1159" rel="#L1159">1159</span>
<span id="L1160" rel="#L1160">1160</span>
<span id="L1161" rel="#L1161">1161</span>
<span id="L1162" rel="#L1162">1162</span>
<span id="L1163" rel="#L1163">1163</span>
<span id="L1164" rel="#L1164">1164</span>
<span id="L1165" rel="#L1165">1165</span>
<span id="L1166" rel="#L1166">1166</span>
<span id="L1167" rel="#L1167">1167</span>
<span id="L1168" rel="#L1168">1168</span>
<span id="L1169" rel="#L1169">1169</span>
<span id="L1170" rel="#L1170">1170</span>
<span id="L1171" rel="#L1171">1171</span>
<span id="L1172" rel="#L1172">1172</span>
<span id="L1173" rel="#L1173">1173</span>
<span id="L1174" rel="#L1174">1174</span>
<span id="L1175" rel="#L1175">1175</span>
<span id="L1176" rel="#L1176">1176</span>
<span id="L1177" rel="#L1177">1177</span>
<span id="L1178" rel="#L1178">1178</span>
<span id="L1179" rel="#L1179">1179</span>
<span id="L1180" rel="#L1180">1180</span>
<span id="L1181" rel="#L1181">1181</span>
<span id="L1182" rel="#L1182">1182</span>
<span id="L1183" rel="#L1183">1183</span>
<span id="L1184" rel="#L1184">1184</span>
<span id="L1185" rel="#L1185">1185</span>
<span id="L1186" rel="#L1186">1186</span>
<span id="L1187" rel="#L1187">1187</span>
<span id="L1188" rel="#L1188">1188</span>
<span id="L1189" rel="#L1189">1189</span>
<span id="L1190" rel="#L1190">1190</span>
<span id="L1191" rel="#L1191">1191</span>
<span id="L1192" rel="#L1192">1192</span>
<span id="L1193" rel="#L1193">1193</span>
<span id="L1194" rel="#L1194">1194</span>
<span id="L1195" rel="#L1195">1195</span>
<span id="L1196" rel="#L1196">1196</span>
<span id="L1197" rel="#L1197">1197</span>
<span id="L1198" rel="#L1198">1198</span>
<span id="L1199" rel="#L1199">1199</span>
<span id="L1200" rel="#L1200">1200</span>
<span id="L1201" rel="#L1201">1201</span>
<span id="L1202" rel="#L1202">1202</span>
<span id="L1203" rel="#L1203">1203</span>
<span id="L1204" rel="#L1204">1204</span>
<span id="L1205" rel="#L1205">1205</span>
<span id="L1206" rel="#L1206">1206</span>
<span id="L1207" rel="#L1207">1207</span>
<span id="L1208" rel="#L1208">1208</span>
<span id="L1209" rel="#L1209">1209</span>
<span id="L1210" rel="#L1210">1210</span>
<span id="L1211" rel="#L1211">1211</span>
<span id="L1212" rel="#L1212">1212</span>
<span id="L1213" rel="#L1213">1213</span>
<span id="L1214" rel="#L1214">1214</span>
<span id="L1215" rel="#L1215">1215</span>
<span id="L1216" rel="#L1216">1216</span>
<span id="L1217" rel="#L1217">1217</span>
<span id="L1218" rel="#L1218">1218</span>
<span id="L1219" rel="#L1219">1219</span>
<span id="L1220" rel="#L1220">1220</span>
<span id="L1221" rel="#L1221">1221</span>
<span id="L1222" rel="#L1222">1222</span>
<span id="L1223" rel="#L1223">1223</span>
<span id="L1224" rel="#L1224">1224</span>
<span id="L1225" rel="#L1225">1225</span>
<span id="L1226" rel="#L1226">1226</span>
<span id="L1227" rel="#L1227">1227</span>
<span id="L1228" rel="#L1228">1228</span>
<span id="L1229" rel="#L1229">1229</span>
<span id="L1230" rel="#L1230">1230</span>
<span id="L1231" rel="#L1231">1231</span>
<span id="L1232" rel="#L1232">1232</span>
<span id="L1233" rel="#L1233">1233</span>
<span id="L1234" rel="#L1234">1234</span>
<span id="L1235" rel="#L1235">1235</span>
<span id="L1236" rel="#L1236">1236</span>
<span id="L1237" rel="#L1237">1237</span>
<span id="L1238" rel="#L1238">1238</span>
<span id="L1239" rel="#L1239">1239</span>
<span id="L1240" rel="#L1240">1240</span>
<span id="L1241" rel="#L1241">1241</span>
<span id="L1242" rel="#L1242">1242</span>
<span id="L1243" rel="#L1243">1243</span>
<span id="L1244" rel="#L1244">1244</span>
<span id="L1245" rel="#L1245">1245</span>
<span id="L1246" rel="#L1246">1246</span>
<span id="L1247" rel="#L1247">1247</span>
<span id="L1248" rel="#L1248">1248</span>
<span id="L1249" rel="#L1249">1249</span>
<span id="L1250" rel="#L1250">1250</span>
<span id="L1251" rel="#L1251">1251</span>
<span id="L1252" rel="#L1252">1252</span>
<span id="L1253" rel="#L1253">1253</span>
<span id="L1254" rel="#L1254">1254</span>
<span id="L1255" rel="#L1255">1255</span>
<span id="L1256" rel="#L1256">1256</span>
<span id="L1257" rel="#L1257">1257</span>
<span id="L1258" rel="#L1258">1258</span>
<span id="L1259" rel="#L1259">1259</span>
<span id="L1260" rel="#L1260">1260</span>
<span id="L1261" rel="#L1261">1261</span>
<span id="L1262" rel="#L1262">1262</span>
<span id="L1263" rel="#L1263">1263</span>
<span id="L1264" rel="#L1264">1264</span>
<span id="L1265" rel="#L1265">1265</span>
<span id="L1266" rel="#L1266">1266</span>
<span id="L1267" rel="#L1267">1267</span>
<span id="L1268" rel="#L1268">1268</span>
<span id="L1269" rel="#L1269">1269</span>
<span id="L1270" rel="#L1270">1270</span>
<span id="L1271" rel="#L1271">1271</span>
<span id="L1272" rel="#L1272">1272</span>
<span id="L1273" rel="#L1273">1273</span>
<span id="L1274" rel="#L1274">1274</span>
<span id="L1275" rel="#L1275">1275</span>
<span id="L1276" rel="#L1276">1276</span>
<span id="L1277" rel="#L1277">1277</span>
<span id="L1278" rel="#L1278">1278</span>
<span id="L1279" rel="#L1279">1279</span>
<span id="L1280" rel="#L1280">1280</span>
<span id="L1281" rel="#L1281">1281</span>
<span id="L1282" rel="#L1282">1282</span>
<span id="L1283" rel="#L1283">1283</span>
<span id="L1284" rel="#L1284">1284</span>
<span id="L1285" rel="#L1285">1285</span>
<span id="L1286" rel="#L1286">1286</span>
<span id="L1287" rel="#L1287">1287</span>
<span id="L1288" rel="#L1288">1288</span>
<span id="L1289" rel="#L1289">1289</span>
<span id="L1290" rel="#L1290">1290</span>
<span id="L1291" rel="#L1291">1291</span>
<span id="L1292" rel="#L1292">1292</span>
<span id="L1293" rel="#L1293">1293</span>
<span id="L1294" rel="#L1294">1294</span>
<span id="L1295" rel="#L1295">1295</span>
<span id="L1296" rel="#L1296">1296</span>
<span id="L1297" rel="#L1297">1297</span>
<span id="L1298" rel="#L1298">1298</span>
<span id="L1299" rel="#L1299">1299</span>
<span id="L1300" rel="#L1300">1300</span>
<span id="L1301" rel="#L1301">1301</span>
<span id="L1302" rel="#L1302">1302</span>
<span id="L1303" rel="#L1303">1303</span>
<span id="L1304" rel="#L1304">1304</span>
<span id="L1305" rel="#L1305">1305</span>
<span id="L1306" rel="#L1306">1306</span>
<span id="L1307" rel="#L1307">1307</span>
<span id="L1308" rel="#L1308">1308</span>
<span id="L1309" rel="#L1309">1309</span>
<span id="L1310" rel="#L1310">1310</span>
<span id="L1311" rel="#L1311">1311</span>
<span id="L1312" rel="#L1312">1312</span>
<span id="L1313" rel="#L1313">1313</span>
<span id="L1314" rel="#L1314">1314</span>
<span id="L1315" rel="#L1315">1315</span>
<span id="L1316" rel="#L1316">1316</span>
<span id="L1317" rel="#L1317">1317</span>
<span id="L1318" rel="#L1318">1318</span>
<span id="L1319" rel="#L1319">1319</span>
<span id="L1320" rel="#L1320">1320</span>
<span id="L1321" rel="#L1321">1321</span>
<span id="L1322" rel="#L1322">1322</span>
<span id="L1323" rel="#L1323">1323</span>
<span id="L1324" rel="#L1324">1324</span>
<span id="L1325" rel="#L1325">1325</span>
<span id="L1326" rel="#L1326">1326</span>
<span id="L1327" rel="#L1327">1327</span>
<span id="L1328" rel="#L1328">1328</span>
<span id="L1329" rel="#L1329">1329</span>
<span id="L1330" rel="#L1330">1330</span>
<span id="L1331" rel="#L1331">1331</span>
<span id="L1332" rel="#L1332">1332</span>
<span id="L1333" rel="#L1333">1333</span>
<span id="L1334" rel="#L1334">1334</span>
<span id="L1335" rel="#L1335">1335</span>
<span id="L1336" rel="#L1336">1336</span>
<span id="L1337" rel="#L1337">1337</span>
<span id="L1338" rel="#L1338">1338</span>
<span id="L1339" rel="#L1339">1339</span>
<span id="L1340" rel="#L1340">1340</span>
<span id="L1341" rel="#L1341">1341</span>
<span id="L1342" rel="#L1342">1342</span>
<span id="L1343" rel="#L1343">1343</span>
<span id="L1344" rel="#L1344">1344</span>
<span id="L1345" rel="#L1345">1345</span>
<span id="L1346" rel="#L1346">1346</span>
<span id="L1347" rel="#L1347">1347</span>
<span id="L1348" rel="#L1348">1348</span>
<span id="L1349" rel="#L1349">1349</span>
<span id="L1350" rel="#L1350">1350</span>
<span id="L1351" rel="#L1351">1351</span>
<span id="L1352" rel="#L1352">1352</span>
<span id="L1353" rel="#L1353">1353</span>
<span id="L1354" rel="#L1354">1354</span>
<span id="L1355" rel="#L1355">1355</span>
<span id="L1356" rel="#L1356">1356</span>
<span id="L1357" rel="#L1357">1357</span>
<span id="L1358" rel="#L1358">1358</span>
<span id="L1359" rel="#L1359">1359</span>
<span id="L1360" rel="#L1360">1360</span>
<span id="L1361" rel="#L1361">1361</span>
<span id="L1362" rel="#L1362">1362</span>
<span id="L1363" rel="#L1363">1363</span>
<span id="L1364" rel="#L1364">1364</span>
<span id="L1365" rel="#L1365">1365</span>
<span id="L1366" rel="#L1366">1366</span>
<span id="L1367" rel="#L1367">1367</span>
<span id="L1368" rel="#L1368">1368</span>
<span id="L1369" rel="#L1369">1369</span>
<span id="L1370" rel="#L1370">1370</span>
<span id="L1371" rel="#L1371">1371</span>
<span id="L1372" rel="#L1372">1372</span>
<span id="L1373" rel="#L1373">1373</span>
<span id="L1374" rel="#L1374">1374</span>
<span id="L1375" rel="#L1375">1375</span>
<span id="L1376" rel="#L1376">1376</span>
<span id="L1377" rel="#L1377">1377</span>
<span id="L1378" rel="#L1378">1378</span>
<span id="L1379" rel="#L1379">1379</span>
<span id="L1380" rel="#L1380">1380</span>
<span id="L1381" rel="#L1381">1381</span>
<span id="L1382" rel="#L1382">1382</span>
<span id="L1383" rel="#L1383">1383</span>
<span id="L1384" rel="#L1384">1384</span>
<span id="L1385" rel="#L1385">1385</span>
<span id="L1386" rel="#L1386">1386</span>
<span id="L1387" rel="#L1387">1387</span>
<span id="L1388" rel="#L1388">1388</span>
<span id="L1389" rel="#L1389">1389</span>
<span id="L1390" rel="#L1390">1390</span>
<span id="L1391" rel="#L1391">1391</span>
<span id="L1392" rel="#L1392">1392</span>
<span id="L1393" rel="#L1393">1393</span>
<span id="L1394" rel="#L1394">1394</span>
<span id="L1395" rel="#L1395">1395</span>
<span id="L1396" rel="#L1396">1396</span>
<span id="L1397" rel="#L1397">1397</span>
<span id="L1398" rel="#L1398">1398</span>
<span id="L1399" rel="#L1399">1399</span>
<span id="L1400" rel="#L1400">1400</span>
<span id="L1401" rel="#L1401">1401</span>
<span id="L1402" rel="#L1402">1402</span>
<span id="L1403" rel="#L1403">1403</span>
<span id="L1404" rel="#L1404">1404</span>
<span id="L1405" rel="#L1405">1405</span>
<span id="L1406" rel="#L1406">1406</span>
<span id="L1407" rel="#L1407">1407</span>
<span id="L1408" rel="#L1408">1408</span>
<span id="L1409" rel="#L1409">1409</span>
<span id="L1410" rel="#L1410">1410</span>
<span id="L1411" rel="#L1411">1411</span>
<span id="L1412" rel="#L1412">1412</span>
<span id="L1413" rel="#L1413">1413</span>
<span id="L1414" rel="#L1414">1414</span>
<span id="L1415" rel="#L1415">1415</span>
<span id="L1416" rel="#L1416">1416</span>
<span id="L1417" rel="#L1417">1417</span>
<span id="L1418" rel="#L1418">1418</span>
<span id="L1419" rel="#L1419">1419</span>
<span id="L1420" rel="#L1420">1420</span>
<span id="L1421" rel="#L1421">1421</span>
<span id="L1422" rel="#L1422">1422</span>
<span id="L1423" rel="#L1423">1423</span>
<span id="L1424" rel="#L1424">1424</span>
<span id="L1425" rel="#L1425">1425</span>
<span id="L1426" rel="#L1426">1426</span>
<span id="L1427" rel="#L1427">1427</span>
<span id="L1428" rel="#L1428">1428</span>
<span id="L1429" rel="#L1429">1429</span>
<span id="L1430" rel="#L1430">1430</span>
<span id="L1431" rel="#L1431">1431</span>
<span id="L1432" rel="#L1432">1432</span>
<span id="L1433" rel="#L1433">1433</span>
<span id="L1434" rel="#L1434">1434</span>
<span id="L1435" rel="#L1435">1435</span>
<span id="L1436" rel="#L1436">1436</span>
<span id="L1437" rel="#L1437">1437</span>
<span id="L1438" rel="#L1438">1438</span>
<span id="L1439" rel="#L1439">1439</span>
<span id="L1440" rel="#L1440">1440</span>
<span id="L1441" rel="#L1441">1441</span>
<span id="L1442" rel="#L1442">1442</span>
<span id="L1443" rel="#L1443">1443</span>
<span id="L1444" rel="#L1444">1444</span>
<span id="L1445" rel="#L1445">1445</span>
<span id="L1446" rel="#L1446">1446</span>
<span id="L1447" rel="#L1447">1447</span>
<span id="L1448" rel="#L1448">1448</span>
<span id="L1449" rel="#L1449">1449</span>
<span id="L1450" rel="#L1450">1450</span>
<span id="L1451" rel="#L1451">1451</span>
<span id="L1452" rel="#L1452">1452</span>
<span id="L1453" rel="#L1453">1453</span>
<span id="L1454" rel="#L1454">1454</span>
<span id="L1455" rel="#L1455">1455</span>
<span id="L1456" rel="#L1456">1456</span>
<span id="L1457" rel="#L1457">1457</span>
<span id="L1458" rel="#L1458">1458</span>
<span id="L1459" rel="#L1459">1459</span>
<span id="L1460" rel="#L1460">1460</span>
<span id="L1461" rel="#L1461">1461</span>
<span id="L1462" rel="#L1462">1462</span>
<span id="L1463" rel="#L1463">1463</span>
<span id="L1464" rel="#L1464">1464</span>
<span id="L1465" rel="#L1465">1465</span>
<span id="L1466" rel="#L1466">1466</span>
<span id="L1467" rel="#L1467">1467</span>
<span id="L1468" rel="#L1468">1468</span>
<span id="L1469" rel="#L1469">1469</span>
<span id="L1470" rel="#L1470">1470</span>
<span id="L1471" rel="#L1471">1471</span>
<span id="L1472" rel="#L1472">1472</span>
<span id="L1473" rel="#L1473">1473</span>
<span id="L1474" rel="#L1474">1474</span>
<span id="L1475" rel="#L1475">1475</span>
<span id="L1476" rel="#L1476">1476</span>
<span id="L1477" rel="#L1477">1477</span>
<span id="L1478" rel="#L1478">1478</span>
<span id="L1479" rel="#L1479">1479</span>
<span id="L1480" rel="#L1480">1480</span>
<span id="L1481" rel="#L1481">1481</span>
<span id="L1482" rel="#L1482">1482</span>
<span id="L1483" rel="#L1483">1483</span>
<span id="L1484" rel="#L1484">1484</span>
<span id="L1485" rel="#L1485">1485</span>
<span id="L1486" rel="#L1486">1486</span>
<span id="L1487" rel="#L1487">1487</span>
<span id="L1488" rel="#L1488">1488</span>
<span id="L1489" rel="#L1489">1489</span>
<span id="L1490" rel="#L1490">1490</span>
<span id="L1491" rel="#L1491">1491</span>
<span id="L1492" rel="#L1492">1492</span>
<span id="L1493" rel="#L1493">1493</span>
<span id="L1494" rel="#L1494">1494</span>
<span id="L1495" rel="#L1495">1495</span>
<span id="L1496" rel="#L1496">1496</span>
<span id="L1497" rel="#L1497">1497</span>
<span id="L1498" rel="#L1498">1498</span>
<span id="L1499" rel="#L1499">1499</span>
<span id="L1500" rel="#L1500">1500</span>
<span id="L1501" rel="#L1501">1501</span>
<span id="L1502" rel="#L1502">1502</span>
<span id="L1503" rel="#L1503">1503</span>
<span id="L1504" rel="#L1504">1504</span>
<span id="L1505" rel="#L1505">1505</span>
<span id="L1506" rel="#L1506">1506</span>
<span id="L1507" rel="#L1507">1507</span>
<span id="L1508" rel="#L1508">1508</span>
<span id="L1509" rel="#L1509">1509</span>
<span id="L1510" rel="#L1510">1510</span>
<span id="L1511" rel="#L1511">1511</span>
<span id="L1512" rel="#L1512">1512</span>
<span id="L1513" rel="#L1513">1513</span>
<span id="L1514" rel="#L1514">1514</span>
<span id="L1515" rel="#L1515">1515</span>
<span id="L1516" rel="#L1516">1516</span>
<span id="L1517" rel="#L1517">1517</span>
<span id="L1518" rel="#L1518">1518</span>
<span id="L1519" rel="#L1519">1519</span>
<span id="L1520" rel="#L1520">1520</span>
<span id="L1521" rel="#L1521">1521</span>
<span id="L1522" rel="#L1522">1522</span>
<span id="L1523" rel="#L1523">1523</span>
<span id="L1524" rel="#L1524">1524</span>
<span id="L1525" rel="#L1525">1525</span>
<span id="L1526" rel="#L1526">1526</span>
<span id="L1527" rel="#L1527">1527</span>
<span id="L1528" rel="#L1528">1528</span>
<span id="L1529" rel="#L1529">1529</span>
<span id="L1530" rel="#L1530">1530</span>
<span id="L1531" rel="#L1531">1531</span>
<span id="L1532" rel="#L1532">1532</span>
<span id="L1533" rel="#L1533">1533</span>
<span id="L1534" rel="#L1534">1534</span>
<span id="L1535" rel="#L1535">1535</span>
<span id="L1536" rel="#L1536">1536</span>
<span id="L1537" rel="#L1537">1537</span>
<span id="L1538" rel="#L1538">1538</span>
<span id="L1539" rel="#L1539">1539</span>
<span id="L1540" rel="#L1540">1540</span>
<span id="L1541" rel="#L1541">1541</span>
<span id="L1542" rel="#L1542">1542</span>
<span id="L1543" rel="#L1543">1543</span>
<span id="L1544" rel="#L1544">1544</span>
<span id="L1545" rel="#L1545">1545</span>
<span id="L1546" rel="#L1546">1546</span>
<span id="L1547" rel="#L1547">1547</span>
<span id="L1548" rel="#L1548">1548</span>
<span id="L1549" rel="#L1549">1549</span>
<span id="L1550" rel="#L1550">1550</span>
<span id="L1551" rel="#L1551">1551</span>
<span id="L1552" rel="#L1552">1552</span>
<span id="L1553" rel="#L1553">1553</span>
<span id="L1554" rel="#L1554">1554</span>
<span id="L1555" rel="#L1555">1555</span>
<span id="L1556" rel="#L1556">1556</span>
<span id="L1557" rel="#L1557">1557</span>
<span id="L1558" rel="#L1558">1558</span>
<span id="L1559" rel="#L1559">1559</span>
<span id="L1560" rel="#L1560">1560</span>
<span id="L1561" rel="#L1561">1561</span>
<span id="L1562" rel="#L1562">1562</span>
<span id="L1563" rel="#L1563">1563</span>
<span id="L1564" rel="#L1564">1564</span>
<span id="L1565" rel="#L1565">1565</span>
<span id="L1566" rel="#L1566">1566</span>
<span id="L1567" rel="#L1567">1567</span>
<span id="L1568" rel="#L1568">1568</span>
<span id="L1569" rel="#L1569">1569</span>
<span id="L1570" rel="#L1570">1570</span>
<span id="L1571" rel="#L1571">1571</span>
<span id="L1572" rel="#L1572">1572</span>
<span id="L1573" rel="#L1573">1573</span>
<span id="L1574" rel="#L1574">1574</span>
<span id="L1575" rel="#L1575">1575</span>
<span id="L1576" rel="#L1576">1576</span>
<span id="L1577" rel="#L1577">1577</span>
<span id="L1578" rel="#L1578">1578</span>
<span id="L1579" rel="#L1579">1579</span>
<span id="L1580" rel="#L1580">1580</span>
<span id="L1581" rel="#L1581">1581</span>
<span id="L1582" rel="#L1582">1582</span>
<span id="L1583" rel="#L1583">1583</span>
<span id="L1584" rel="#L1584">1584</span>
<span id="L1585" rel="#L1585">1585</span>
<span id="L1586" rel="#L1586">1586</span>
<span id="L1587" rel="#L1587">1587</span>
<span id="L1588" rel="#L1588">1588</span>
<span id="L1589" rel="#L1589">1589</span>
<span id="L1590" rel="#L1590">1590</span>
<span id="L1591" rel="#L1591">1591</span>
<span id="L1592" rel="#L1592">1592</span>
<span id="L1593" rel="#L1593">1593</span>
<span id="L1594" rel="#L1594">1594</span>
<span id="L1595" rel="#L1595">1595</span>
<span id="L1596" rel="#L1596">1596</span>
<span id="L1597" rel="#L1597">1597</span>
<span id="L1598" rel="#L1598">1598</span>
<span id="L1599" rel="#L1599">1599</span>
<span id="L1600" rel="#L1600">1600</span>
<span id="L1601" rel="#L1601">1601</span>
<span id="L1602" rel="#L1602">1602</span>
<span id="L1603" rel="#L1603">1603</span>
<span id="L1604" rel="#L1604">1604</span>
<span id="L1605" rel="#L1605">1605</span>
<span id="L1606" rel="#L1606">1606</span>
<span id="L1607" rel="#L1607">1607</span>
<span id="L1608" rel="#L1608">1608</span>
<span id="L1609" rel="#L1609">1609</span>
<span id="L1610" rel="#L1610">1610</span>
<span id="L1611" rel="#L1611">1611</span>
<span id="L1612" rel="#L1612">1612</span>
<span id="L1613" rel="#L1613">1613</span>
<span id="L1614" rel="#L1614">1614</span>
<span id="L1615" rel="#L1615">1615</span>
<span id="L1616" rel="#L1616">1616</span>
<span id="L1617" rel="#L1617">1617</span>
<span id="L1618" rel="#L1618">1618</span>
<span id="L1619" rel="#L1619">1619</span>
<span id="L1620" rel="#L1620">1620</span>
<span id="L1621" rel="#L1621">1621</span>
<span id="L1622" rel="#L1622">1622</span>
<span id="L1623" rel="#L1623">1623</span>
<span id="L1624" rel="#L1624">1624</span>
<span id="L1625" rel="#L1625">1625</span>
<span id="L1626" rel="#L1626">1626</span>
<span id="L1627" rel="#L1627">1627</span>
<span id="L1628" rel="#L1628">1628</span>
<span id="L1629" rel="#L1629">1629</span>
<span id="L1630" rel="#L1630">1630</span>
<span id="L1631" rel="#L1631">1631</span>
<span id="L1632" rel="#L1632">1632</span>
<span id="L1633" rel="#L1633">1633</span>
<span id="L1634" rel="#L1634">1634</span>
<span id="L1635" rel="#L1635">1635</span>
<span id="L1636" rel="#L1636">1636</span>
<span id="L1637" rel="#L1637">1637</span>
<span id="L1638" rel="#L1638">1638</span>
<span id="L1639" rel="#L1639">1639</span>
<span id="L1640" rel="#L1640">1640</span>
<span id="L1641" rel="#L1641">1641</span>
<span id="L1642" rel="#L1642">1642</span>
<span id="L1643" rel="#L1643">1643</span>
<span id="L1644" rel="#L1644">1644</span>
<span id="L1645" rel="#L1645">1645</span>
<span id="L1646" rel="#L1646">1646</span>
<span id="L1647" rel="#L1647">1647</span>
<span id="L1648" rel="#L1648">1648</span>
<span id="L1649" rel="#L1649">1649</span>
<span id="L1650" rel="#L1650">1650</span>
<span id="L1651" rel="#L1651">1651</span>
<span id="L1652" rel="#L1652">1652</span>
<span id="L1653" rel="#L1653">1653</span>
<span id="L1654" rel="#L1654">1654</span>
<span id="L1655" rel="#L1655">1655</span>
<span id="L1656" rel="#L1656">1656</span>
<span id="L1657" rel="#L1657">1657</span>
<span id="L1658" rel="#L1658">1658</span>
<span id="L1659" rel="#L1659">1659</span>
<span id="L1660" rel="#L1660">1660</span>
<span id="L1661" rel="#L1661">1661</span>
<span id="L1662" rel="#L1662">1662</span>
<span id="L1663" rel="#L1663">1663</span>
<span id="L1664" rel="#L1664">1664</span>
<span id="L1665" rel="#L1665">1665</span>
<span id="L1666" rel="#L1666">1666</span>
<span id="L1667" rel="#L1667">1667</span>
<span id="L1668" rel="#L1668">1668</span>
<span id="L1669" rel="#L1669">1669</span>
<span id="L1670" rel="#L1670">1670</span>
<span id="L1671" rel="#L1671">1671</span>
<span id="L1672" rel="#L1672">1672</span>
<span id="L1673" rel="#L1673">1673</span>
<span id="L1674" rel="#L1674">1674</span>
<span id="L1675" rel="#L1675">1675</span>
<span id="L1676" rel="#L1676">1676</span>
<span id="L1677" rel="#L1677">1677</span>
<span id="L1678" rel="#L1678">1678</span>
<span id="L1679" rel="#L1679">1679</span>
<span id="L1680" rel="#L1680">1680</span>
<span id="L1681" rel="#L1681">1681</span>
<span id="L1682" rel="#L1682">1682</span>
<span id="L1683" rel="#L1683">1683</span>
<span id="L1684" rel="#L1684">1684</span>
<span id="L1685" rel="#L1685">1685</span>
<span id="L1686" rel="#L1686">1686</span>
<span id="L1687" rel="#L1687">1687</span>
<span id="L1688" rel="#L1688">1688</span>
<span id="L1689" rel="#L1689">1689</span>
<span id="L1690" rel="#L1690">1690</span>
<span id="L1691" rel="#L1691">1691</span>
<span id="L1692" rel="#L1692">1692</span>
<span id="L1693" rel="#L1693">1693</span>
<span id="L1694" rel="#L1694">1694</span>
<span id="L1695" rel="#L1695">1695</span>
<span id="L1696" rel="#L1696">1696</span>
<span id="L1697" rel="#L1697">1697</span>
<span id="L1698" rel="#L1698">1698</span>
<span id="L1699" rel="#L1699">1699</span>
<span id="L1700" rel="#L1700">1700</span>
<span id="L1701" rel="#L1701">1701</span>
<span id="L1702" rel="#L1702">1702</span>
<span id="L1703" rel="#L1703">1703</span>
<span id="L1704" rel="#L1704">1704</span>
<span id="L1705" rel="#L1705">1705</span>
<span id="L1706" rel="#L1706">1706</span>
<span id="L1707" rel="#L1707">1707</span>
<span id="L1708" rel="#L1708">1708</span>
<span id="L1709" rel="#L1709">1709</span>
<span id="L1710" rel="#L1710">1710</span>
<span id="L1711" rel="#L1711">1711</span>
<span id="L1712" rel="#L1712">1712</span>
<span id="L1713" rel="#L1713">1713</span>
<span id="L1714" rel="#L1714">1714</span>
<span id="L1715" rel="#L1715">1715</span>
<span id="L1716" rel="#L1716">1716</span>
<span id="L1717" rel="#L1717">1717</span>
<span id="L1718" rel="#L1718">1718</span>
<span id="L1719" rel="#L1719">1719</span>
<span id="L1720" rel="#L1720">1720</span>
<span id="L1721" rel="#L1721">1721</span>
<span id="L1722" rel="#L1722">1722</span>
<span id="L1723" rel="#L1723">1723</span>
<span id="L1724" rel="#L1724">1724</span>
<span id="L1725" rel="#L1725">1725</span>
<span id="L1726" rel="#L1726">1726</span>
<span id="L1727" rel="#L1727">1727</span>
<span id="L1728" rel="#L1728">1728</span>
<span id="L1729" rel="#L1729">1729</span>
<span id="L1730" rel="#L1730">1730</span>
<span id="L1731" rel="#L1731">1731</span>
<span id="L1732" rel="#L1732">1732</span>
<span id="L1733" rel="#L1733">1733</span>
<span id="L1734" rel="#L1734">1734</span>
<span id="L1735" rel="#L1735">1735</span>
<span id="L1736" rel="#L1736">1736</span>
<span id="L1737" rel="#L1737">1737</span>
<span id="L1738" rel="#L1738">1738</span>
<span id="L1739" rel="#L1739">1739</span>
<span id="L1740" rel="#L1740">1740</span>
<span id="L1741" rel="#L1741">1741</span>
<span id="L1742" rel="#L1742">1742</span>
<span id="L1743" rel="#L1743">1743</span>
<span id="L1744" rel="#L1744">1744</span>
<span id="L1745" rel="#L1745">1745</span>
<span id="L1746" rel="#L1746">1746</span>
<span id="L1747" rel="#L1747">1747</span>
<span id="L1748" rel="#L1748">1748</span>
<span id="L1749" rel="#L1749">1749</span>
<span id="L1750" rel="#L1750">1750</span>
<span id="L1751" rel="#L1751">1751</span>
<span id="L1752" rel="#L1752">1752</span>
<span id="L1753" rel="#L1753">1753</span>
<span id="L1754" rel="#L1754">1754</span>
<span id="L1755" rel="#L1755">1755</span>
<span id="L1756" rel="#L1756">1756</span>
<span id="L1757" rel="#L1757">1757</span>
<span id="L1758" rel="#L1758">1758</span>
<span id="L1759" rel="#L1759">1759</span>
<span id="L1760" rel="#L1760">1760</span>
<span id="L1761" rel="#L1761">1761</span>
<span id="L1762" rel="#L1762">1762</span>
<span id="L1763" rel="#L1763">1763</span>
<span id="L1764" rel="#L1764">1764</span>
<span id="L1765" rel="#L1765">1765</span>
<span id="L1766" rel="#L1766">1766</span>
<span id="L1767" rel="#L1767">1767</span>
<span id="L1768" rel="#L1768">1768</span>
<span id="L1769" rel="#L1769">1769</span>
<span id="L1770" rel="#L1770">1770</span>
<span id="L1771" rel="#L1771">1771</span>
<span id="L1772" rel="#L1772">1772</span>
<span id="L1773" rel="#L1773">1773</span>
<span id="L1774" rel="#L1774">1774</span>
<span id="L1775" rel="#L1775">1775</span>
<span id="L1776" rel="#L1776">1776</span>
<span id="L1777" rel="#L1777">1777</span>
<span id="L1778" rel="#L1778">1778</span>
<span id="L1779" rel="#L1779">1779</span>
<span id="L1780" rel="#L1780">1780</span>
<span id="L1781" rel="#L1781">1781</span>
<span id="L1782" rel="#L1782">1782</span>
<span id="L1783" rel="#L1783">1783</span>
<span id="L1784" rel="#L1784">1784</span>
<span id="L1785" rel="#L1785">1785</span>
<span id="L1786" rel="#L1786">1786</span>
<span id="L1787" rel="#L1787">1787</span>
<span id="L1788" rel="#L1788">1788</span>
<span id="L1789" rel="#L1789">1789</span>
<span id="L1790" rel="#L1790">1790</span>
<span id="L1791" rel="#L1791">1791</span>
<span id="L1792" rel="#L1792">1792</span>
<span id="L1793" rel="#L1793">1793</span>
<span id="L1794" rel="#L1794">1794</span>
<span id="L1795" rel="#L1795">1795</span>
<span id="L1796" rel="#L1796">1796</span>
<span id="L1797" rel="#L1797">1797</span>
<span id="L1798" rel="#L1798">1798</span>
<span id="L1799" rel="#L1799">1799</span>
<span id="L1800" rel="#L1800">1800</span>
<span id="L1801" rel="#L1801">1801</span>
<span id="L1802" rel="#L1802">1802</span>
<span id="L1803" rel="#L1803">1803</span>
<span id="L1804" rel="#L1804">1804</span>
<span id="L1805" rel="#L1805">1805</span>
<span id="L1806" rel="#L1806">1806</span>
<span id="L1807" rel="#L1807">1807</span>
<span id="L1808" rel="#L1808">1808</span>
<span id="L1809" rel="#L1809">1809</span>
<span id="L1810" rel="#L1810">1810</span>
<span id="L1811" rel="#L1811">1811</span>
<span id="L1812" rel="#L1812">1812</span>
<span id="L1813" rel="#L1813">1813</span>
<span id="L1814" rel="#L1814">1814</span>
<span id="L1815" rel="#L1815">1815</span>
<span id="L1816" rel="#L1816">1816</span>
<span id="L1817" rel="#L1817">1817</span>
<span id="L1818" rel="#L1818">1818</span>
<span id="L1819" rel="#L1819">1819</span>
<span id="L1820" rel="#L1820">1820</span>
<span id="L1821" rel="#L1821">1821</span>
<span id="L1822" rel="#L1822">1822</span>
<span id="L1823" rel="#L1823">1823</span>
<span id="L1824" rel="#L1824">1824</span>
<span id="L1825" rel="#L1825">1825</span>
<span id="L1826" rel="#L1826">1826</span>
<span id="L1827" rel="#L1827">1827</span>
<span id="L1828" rel="#L1828">1828</span>
<span id="L1829" rel="#L1829">1829</span>
<span id="L1830" rel="#L1830">1830</span>
<span id="L1831" rel="#L1831">1831</span>
<span id="L1832" rel="#L1832">1832</span>
<span id="L1833" rel="#L1833">1833</span>
<span id="L1834" rel="#L1834">1834</span>
<span id="L1835" rel="#L1835">1835</span>
<span id="L1836" rel="#L1836">1836</span>
<span id="L1837" rel="#L1837">1837</span>
<span id="L1838" rel="#L1838">1838</span>
<span id="L1839" rel="#L1839">1839</span>
<span id="L1840" rel="#L1840">1840</span>
<span id="L1841" rel="#L1841">1841</span>
<span id="L1842" rel="#L1842">1842</span>
<span id="L1843" rel="#L1843">1843</span>
<span id="L1844" rel="#L1844">1844</span>
<span id="L1845" rel="#L1845">1845</span>
<span id="L1846" rel="#L1846">1846</span>
<span id="L1847" rel="#L1847">1847</span>
<span id="L1848" rel="#L1848">1848</span>
<span id="L1849" rel="#L1849">1849</span>
<span id="L1850" rel="#L1850">1850</span>
<span id="L1851" rel="#L1851">1851</span>
<span id="L1852" rel="#L1852">1852</span>
<span id="L1853" rel="#L1853">1853</span>
<span id="L1854" rel="#L1854">1854</span>
<span id="L1855" rel="#L1855">1855</span>
<span id="L1856" rel="#L1856">1856</span>
<span id="L1857" rel="#L1857">1857</span>
<span id="L1858" rel="#L1858">1858</span>
<span id="L1859" rel="#L1859">1859</span>
<span id="L1860" rel="#L1860">1860</span>
<span id="L1861" rel="#L1861">1861</span>
<span id="L1862" rel="#L1862">1862</span>
<span id="L1863" rel="#L1863">1863</span>
<span id="L1864" rel="#L1864">1864</span>
<span id="L1865" rel="#L1865">1865</span>
<span id="L1866" rel="#L1866">1866</span>
<span id="L1867" rel="#L1867">1867</span>
<span id="L1868" rel="#L1868">1868</span>
<span id="L1869" rel="#L1869">1869</span>
<span id="L1870" rel="#L1870">1870</span>
<span id="L1871" rel="#L1871">1871</span>
<span id="L1872" rel="#L1872">1872</span>
<span id="L1873" rel="#L1873">1873</span>
<span id="L1874" rel="#L1874">1874</span>
<span id="L1875" rel="#L1875">1875</span>
<span id="L1876" rel="#L1876">1876</span>
<span id="L1877" rel="#L1877">1877</span>
<span id="L1878" rel="#L1878">1878</span>
<span id="L1879" rel="#L1879">1879</span>
<span id="L1880" rel="#L1880">1880</span>
<span id="L1881" rel="#L1881">1881</span>
<span id="L1882" rel="#L1882">1882</span>
<span id="L1883" rel="#L1883">1883</span>
<span id="L1884" rel="#L1884">1884</span>
<span id="L1885" rel="#L1885">1885</span>
<span id="L1886" rel="#L1886">1886</span>
<span id="L1887" rel="#L1887">1887</span>
<span id="L1888" rel="#L1888">1888</span>
<span id="L1889" rel="#L1889">1889</span>
<span id="L1890" rel="#L1890">1890</span>
<span id="L1891" rel="#L1891">1891</span>
<span id="L1892" rel="#L1892">1892</span>
<span id="L1893" rel="#L1893">1893</span>
<span id="L1894" rel="#L1894">1894</span>
<span id="L1895" rel="#L1895">1895</span>
<span id="L1896" rel="#L1896">1896</span>
<span id="L1897" rel="#L1897">1897</span>
<span id="L1898" rel="#L1898">1898</span>
<span id="L1899" rel="#L1899">1899</span>
<span id="L1900" rel="#L1900">1900</span>
<span id="L1901" rel="#L1901">1901</span>
<span id="L1902" rel="#L1902">1902</span>
<span id="L1903" rel="#L1903">1903</span>
<span id="L1904" rel="#L1904">1904</span>
<span id="L1905" rel="#L1905">1905</span>
<span id="L1906" rel="#L1906">1906</span>
<span id="L1907" rel="#L1907">1907</span>
<span id="L1908" rel="#L1908">1908</span>
<span id="L1909" rel="#L1909">1909</span>
<span id="L1910" rel="#L1910">1910</span>
<span id="L1911" rel="#L1911">1911</span>
<span id="L1912" rel="#L1912">1912</span>
<span id="L1913" rel="#L1913">1913</span>
<span id="L1914" rel="#L1914">1914</span>
<span id="L1915" rel="#L1915">1915</span>
<span id="L1916" rel="#L1916">1916</span>
<span id="L1917" rel="#L1917">1917</span>
<span id="L1918" rel="#L1918">1918</span>
<span id="L1919" rel="#L1919">1919</span>
<span id="L1920" rel="#L1920">1920</span>
<span id="L1921" rel="#L1921">1921</span>
<span id="L1922" rel="#L1922">1922</span>
<span id="L1923" rel="#L1923">1923</span>
<span id="L1924" rel="#L1924">1924</span>
<span id="L1925" rel="#L1925">1925</span>
<span id="L1926" rel="#L1926">1926</span>
<span id="L1927" rel="#L1927">1927</span>
<span id="L1928" rel="#L1928">1928</span>
<span id="L1929" rel="#L1929">1929</span>
<span id="L1930" rel="#L1930">1930</span>
<span id="L1931" rel="#L1931">1931</span>
<span id="L1932" rel="#L1932">1932</span>
<span id="L1933" rel="#L1933">1933</span>
<span id="L1934" rel="#L1934">1934</span>
<span id="L1935" rel="#L1935">1935</span>
<span id="L1936" rel="#L1936">1936</span>
<span id="L1937" rel="#L1937">1937</span>
<span id="L1938" rel="#L1938">1938</span>
<span id="L1939" rel="#L1939">1939</span>
<span id="L1940" rel="#L1940">1940</span>
<span id="L1941" rel="#L1941">1941</span>
<span id="L1942" rel="#L1942">1942</span>
<span id="L1943" rel="#L1943">1943</span>
<span id="L1944" rel="#L1944">1944</span>
<span id="L1945" rel="#L1945">1945</span>
<span id="L1946" rel="#L1946">1946</span>
<span id="L1947" rel="#L1947">1947</span>
<span id="L1948" rel="#L1948">1948</span>
<span id="L1949" rel="#L1949">1949</span>
<span id="L1950" rel="#L1950">1950</span>
<span id="L1951" rel="#L1951">1951</span>
<span id="L1952" rel="#L1952">1952</span>
<span id="L1953" rel="#L1953">1953</span>
<span id="L1954" rel="#L1954">1954</span>
<span id="L1955" rel="#L1955">1955</span>
<span id="L1956" rel="#L1956">1956</span>
<span id="L1957" rel="#L1957">1957</span>
<span id="L1958" rel="#L1958">1958</span>
<span id="L1959" rel="#L1959">1959</span>
<span id="L1960" rel="#L1960">1960</span>
<span id="L1961" rel="#L1961">1961</span>
<span id="L1962" rel="#L1962">1962</span>
<span id="L1963" rel="#L1963">1963</span>
<span id="L1964" rel="#L1964">1964</span>
<span id="L1965" rel="#L1965">1965</span>
<span id="L1966" rel="#L1966">1966</span>
<span id="L1967" rel="#L1967">1967</span>
<span id="L1968" rel="#L1968">1968</span>
<span id="L1969" rel="#L1969">1969</span>
<span id="L1970" rel="#L1970">1970</span>
<span id="L1971" rel="#L1971">1971</span>
<span id="L1972" rel="#L1972">1972</span>
<span id="L1973" rel="#L1973">1973</span>
<span id="L1974" rel="#L1974">1974</span>
<span id="L1975" rel="#L1975">1975</span>
<span id="L1976" rel="#L1976">1976</span>
<span id="L1977" rel="#L1977">1977</span>
<span id="L1978" rel="#L1978">1978</span>
<span id="L1979" rel="#L1979">1979</span>
<span id="L1980" rel="#L1980">1980</span>
<span id="L1981" rel="#L1981">1981</span>
<span id="L1982" rel="#L1982">1982</span>
<span id="L1983" rel="#L1983">1983</span>
<span id="L1984" rel="#L1984">1984</span>
<span id="L1985" rel="#L1985">1985</span>
<span id="L1986" rel="#L1986">1986</span>
<span id="L1987" rel="#L1987">1987</span>
<span id="L1988" rel="#L1988">1988</span>
<span id="L1989" rel="#L1989">1989</span>
<span id="L1990" rel="#L1990">1990</span>
<span id="L1991" rel="#L1991">1991</span>
<span id="L1992" rel="#L1992">1992</span>
<span id="L1993" rel="#L1993">1993</span>
<span id="L1994" rel="#L1994">1994</span>
<span id="L1995" rel="#L1995">1995</span>
<span id="L1996" rel="#L1996">1996</span>
<span id="L1997" rel="#L1997">1997</span>
<span id="L1998" rel="#L1998">1998</span>
<span id="L1999" rel="#L1999">1999</span>
<span id="L2000" rel="#L2000">2000</span>
<span id="L2001" rel="#L2001">2001</span>
<span id="L2002" rel="#L2002">2002</span>
<span id="L2003" rel="#L2003">2003</span>
<span id="L2004" rel="#L2004">2004</span>
<span id="L2005" rel="#L2005">2005</span>
<span id="L2006" rel="#L2006">2006</span>
<span id="L2007" rel="#L2007">2007</span>
<span id="L2008" rel="#L2008">2008</span>
<span id="L2009" rel="#L2009">2009</span>
<span id="L2010" rel="#L2010">2010</span>
<span id="L2011" rel="#L2011">2011</span>
<span id="L2012" rel="#L2012">2012</span>
<span id="L2013" rel="#L2013">2013</span>
<span id="L2014" rel="#L2014">2014</span>
<span id="L2015" rel="#L2015">2015</span>
<span id="L2016" rel="#L2016">2016</span>
<span id="L2017" rel="#L2017">2017</span>
<span id="L2018" rel="#L2018">2018</span>
<span id="L2019" rel="#L2019">2019</span>
<span id="L2020" rel="#L2020">2020</span>
<span id="L2021" rel="#L2021">2021</span>
<span id="L2022" rel="#L2022">2022</span>
<span id="L2023" rel="#L2023">2023</span>
<span id="L2024" rel="#L2024">2024</span>
<span id="L2025" rel="#L2025">2025</span>
<span id="L2026" rel="#L2026">2026</span>
<span id="L2027" rel="#L2027">2027</span>
<span id="L2028" rel="#L2028">2028</span>
<span id="L2029" rel="#L2029">2029</span>
<span id="L2030" rel="#L2030">2030</span>
<span id="L2031" rel="#L2031">2031</span>
<span id="L2032" rel="#L2032">2032</span>
<span id="L2033" rel="#L2033">2033</span>
<span id="L2034" rel="#L2034">2034</span>
<span id="L2035" rel="#L2035">2035</span>
<span id="L2036" rel="#L2036">2036</span>
<span id="L2037" rel="#L2037">2037</span>
<span id="L2038" rel="#L2038">2038</span>
<span id="L2039" rel="#L2039">2039</span>
<span id="L2040" rel="#L2040">2040</span>
<span id="L2041" rel="#L2041">2041</span>
<span id="L2042" rel="#L2042">2042</span>
<span id="L2043" rel="#L2043">2043</span>
<span id="L2044" rel="#L2044">2044</span>
<span id="L2045" rel="#L2045">2045</span>
<span id="L2046" rel="#L2046">2046</span>
<span id="L2047" rel="#L2047">2047</span>
<span id="L2048" rel="#L2048">2048</span>
<span id="L2049" rel="#L2049">2049</span>
<span id="L2050" rel="#L2050">2050</span>
<span id="L2051" rel="#L2051">2051</span>
<span id="L2052" rel="#L2052">2052</span>
<span id="L2053" rel="#L2053">2053</span>
<span id="L2054" rel="#L2054">2054</span>
<span id="L2055" rel="#L2055">2055</span>
<span id="L2056" rel="#L2056">2056</span>
<span id="L2057" rel="#L2057">2057</span>
<span id="L2058" rel="#L2058">2058</span>
<span id="L2059" rel="#L2059">2059</span>
<span id="L2060" rel="#L2060">2060</span>
<span id="L2061" rel="#L2061">2061</span>
<span id="L2062" rel="#L2062">2062</span>
<span id="L2063" rel="#L2063">2063</span>
<span id="L2064" rel="#L2064">2064</span>
<span id="L2065" rel="#L2065">2065</span>
<span id="L2066" rel="#L2066">2066</span>
<span id="L2067" rel="#L2067">2067</span>
<span id="L2068" rel="#L2068">2068</span>
<span id="L2069" rel="#L2069">2069</span>
<span id="L2070" rel="#L2070">2070</span>
<span id="L2071" rel="#L2071">2071</span>
<span id="L2072" rel="#L2072">2072</span>
<span id="L2073" rel="#L2073">2073</span>
<span id="L2074" rel="#L2074">2074</span>
<span id="L2075" rel="#L2075">2075</span>
<span id="L2076" rel="#L2076">2076</span>
<span id="L2077" rel="#L2077">2077</span>
<span id="L2078" rel="#L2078">2078</span>
<span id="L2079" rel="#L2079">2079</span>
<span id="L2080" rel="#L2080">2080</span>
<span id="L2081" rel="#L2081">2081</span>
<span id="L2082" rel="#L2082">2082</span>
<span id="L2083" rel="#L2083">2083</span>
<span id="L2084" rel="#L2084">2084</span>
<span id="L2085" rel="#L2085">2085</span>
<span id="L2086" rel="#L2086">2086</span>
<span id="L2087" rel="#L2087">2087</span>
<span id="L2088" rel="#L2088">2088</span>
<span id="L2089" rel="#L2089">2089</span>
<span id="L2090" rel="#L2090">2090</span>
<span id="L2091" rel="#L2091">2091</span>
<span id="L2092" rel="#L2092">2092</span>
<span id="L2093" rel="#L2093">2093</span>
<span id="L2094" rel="#L2094">2094</span>
<span id="L2095" rel="#L2095">2095</span>
<span id="L2096" rel="#L2096">2096</span>
<span id="L2097" rel="#L2097">2097</span>
<span id="L2098" rel="#L2098">2098</span>
<span id="L2099" rel="#L2099">2099</span>
<span id="L2100" rel="#L2100">2100</span>
<span id="L2101" rel="#L2101">2101</span>
<span id="L2102" rel="#L2102">2102</span>
<span id="L2103" rel="#L2103">2103</span>
<span id="L2104" rel="#L2104">2104</span>
<span id="L2105" rel="#L2105">2105</span>
<span id="L2106" rel="#L2106">2106</span>
<span id="L2107" rel="#L2107">2107</span>
<span id="L2108" rel="#L2108">2108</span>
<span id="L2109" rel="#L2109">2109</span>
<span id="L2110" rel="#L2110">2110</span>
<span id="L2111" rel="#L2111">2111</span>
<span id="L2112" rel="#L2112">2112</span>
<span id="L2113" rel="#L2113">2113</span>
<span id="L2114" rel="#L2114">2114</span>
<span id="L2115" rel="#L2115">2115</span>
<span id="L2116" rel="#L2116">2116</span>
<span id="L2117" rel="#L2117">2117</span>
<span id="L2118" rel="#L2118">2118</span>
<span id="L2119" rel="#L2119">2119</span>
<span id="L2120" rel="#L2120">2120</span>
<span id="L2121" rel="#L2121">2121</span>
<span id="L2122" rel="#L2122">2122</span>
<span id="L2123" rel="#L2123">2123</span>
<span id="L2124" rel="#L2124">2124</span>
<span id="L2125" rel="#L2125">2125</span>
<span id="L2126" rel="#L2126">2126</span>
<span id="L2127" rel="#L2127">2127</span>
<span id="L2128" rel="#L2128">2128</span>
<span id="L2129" rel="#L2129">2129</span>
<span id="L2130" rel="#L2130">2130</span>
<span id="L2131" rel="#L2131">2131</span>
<span id="L2132" rel="#L2132">2132</span>
<span id="L2133" rel="#L2133">2133</span>
<span id="L2134" rel="#L2134">2134</span>
<span id="L2135" rel="#L2135">2135</span>
<span id="L2136" rel="#L2136">2136</span>
<span id="L2137" rel="#L2137">2137</span>
<span id="L2138" rel="#L2138">2138</span>
<span id="L2139" rel="#L2139">2139</span>
<span id="L2140" rel="#L2140">2140</span>
<span id="L2141" rel="#L2141">2141</span>
<span id="L2142" rel="#L2142">2142</span>
<span id="L2143" rel="#L2143">2143</span>
<span id="L2144" rel="#L2144">2144</span>
<span id="L2145" rel="#L2145">2145</span>
<span id="L2146" rel="#L2146">2146</span>
<span id="L2147" rel="#L2147">2147</span>
<span id="L2148" rel="#L2148">2148</span>
<span id="L2149" rel="#L2149">2149</span>
<span id="L2150" rel="#L2150">2150</span>
<span id="L2151" rel="#L2151">2151</span>
<span id="L2152" rel="#L2152">2152</span>
<span id="L2153" rel="#L2153">2153</span>
<span id="L2154" rel="#L2154">2154</span>
<span id="L2155" rel="#L2155">2155</span>
<span id="L2156" rel="#L2156">2156</span>
<span id="L2157" rel="#L2157">2157</span>
<span id="L2158" rel="#L2158">2158</span>
<span id="L2159" rel="#L2159">2159</span>
<span id="L2160" rel="#L2160">2160</span>
<span id="L2161" rel="#L2161">2161</span>
<span id="L2162" rel="#L2162">2162</span>
<span id="L2163" rel="#L2163">2163</span>
<span id="L2164" rel="#L2164">2164</span>
<span id="L2165" rel="#L2165">2165</span>
<span id="L2166" rel="#L2166">2166</span>
<span id="L2167" rel="#L2167">2167</span>
<span id="L2168" rel="#L2168">2168</span>
<span id="L2169" rel="#L2169">2169</span>
<span id="L2170" rel="#L2170">2170</span>
<span id="L2171" rel="#L2171">2171</span>
<span id="L2172" rel="#L2172">2172</span>
<span id="L2173" rel="#L2173">2173</span>
<span id="L2174" rel="#L2174">2174</span>
<span id="L2175" rel="#L2175">2175</span>
<span id="L2176" rel="#L2176">2176</span>
<span id="L2177" rel="#L2177">2177</span>
<span id="L2178" rel="#L2178">2178</span>
<span id="L2179" rel="#L2179">2179</span>
<span id="L2180" rel="#L2180">2180</span>
<span id="L2181" rel="#L2181">2181</span>
<span id="L2182" rel="#L2182">2182</span>
<span id="L2183" rel="#L2183">2183</span>
<span id="L2184" rel="#L2184">2184</span>
<span id="L2185" rel="#L2185">2185</span>
<span id="L2186" rel="#L2186">2186</span>
<span id="L2187" rel="#L2187">2187</span>
<span id="L2188" rel="#L2188">2188</span>
<span id="L2189" rel="#L2189">2189</span>
<span id="L2190" rel="#L2190">2190</span>
<span id="L2191" rel="#L2191">2191</span>
<span id="L2192" rel="#L2192">2192</span>
<span id="L2193" rel="#L2193">2193</span>
<span id="L2194" rel="#L2194">2194</span>
<span id="L2195" rel="#L2195">2195</span>
<span id="L2196" rel="#L2196">2196</span>
<span id="L2197" rel="#L2197">2197</span>
<span id="L2198" rel="#L2198">2198</span>
<span id="L2199" rel="#L2199">2199</span>
<span id="L2200" rel="#L2200">2200</span>
<span id="L2201" rel="#L2201">2201</span>
<span id="L2202" rel="#L2202">2202</span>
<span id="L2203" rel="#L2203">2203</span>
<span id="L2204" rel="#L2204">2204</span>
<span id="L2205" rel="#L2205">2205</span>
<span id="L2206" rel="#L2206">2206</span>
<span id="L2207" rel="#L2207">2207</span>
<span id="L2208" rel="#L2208">2208</span>
<span id="L2209" rel="#L2209">2209</span>
<span id="L2210" rel="#L2210">2210</span>
<span id="L2211" rel="#L2211">2211</span>
<span id="L2212" rel="#L2212">2212</span>
<span id="L2213" rel="#L2213">2213</span>
<span id="L2214" rel="#L2214">2214</span>
<span id="L2215" rel="#L2215">2215</span>
<span id="L2216" rel="#L2216">2216</span>
<span id="L2217" rel="#L2217">2217</span>
<span id="L2218" rel="#L2218">2218</span>
<span id="L2219" rel="#L2219">2219</span>
<span id="L2220" rel="#L2220">2220</span>
<span id="L2221" rel="#L2221">2221</span>
<span id="L2222" rel="#L2222">2222</span>
<span id="L2223" rel="#L2223">2223</span>
<span id="L2224" rel="#L2224">2224</span>
<span id="L2225" rel="#L2225">2225</span>
<span id="L2226" rel="#L2226">2226</span>
<span id="L2227" rel="#L2227">2227</span>
<span id="L2228" rel="#L2228">2228</span>
<span id="L2229" rel="#L2229">2229</span>
<span id="L2230" rel="#L2230">2230</span>
<span id="L2231" rel="#L2231">2231</span>
<span id="L2232" rel="#L2232">2232</span>
<span id="L2233" rel="#L2233">2233</span>
<span id="L2234" rel="#L2234">2234</span>
<span id="L2235" rel="#L2235">2235</span>
<span id="L2236" rel="#L2236">2236</span>
<span id="L2237" rel="#L2237">2237</span>
<span id="L2238" rel="#L2238">2238</span>
<span id="L2239" rel="#L2239">2239</span>
<span id="L2240" rel="#L2240">2240</span>
<span id="L2241" rel="#L2241">2241</span>
<span id="L2242" rel="#L2242">2242</span>
<span id="L2243" rel="#L2243">2243</span>
<span id="L2244" rel="#L2244">2244</span>
<span id="L2245" rel="#L2245">2245</span>
<span id="L2246" rel="#L2246">2246</span>
<span id="L2247" rel="#L2247">2247</span>
<span id="L2248" rel="#L2248">2248</span>
<span id="L2249" rel="#L2249">2249</span>
<span id="L2250" rel="#L2250">2250</span>
<span id="L2251" rel="#L2251">2251</span>
<span id="L2252" rel="#L2252">2252</span>
<span id="L2253" rel="#L2253">2253</span>
<span id="L2254" rel="#L2254">2254</span>
<span id="L2255" rel="#L2255">2255</span>
<span id="L2256" rel="#L2256">2256</span>
<span id="L2257" rel="#L2257">2257</span>
<span id="L2258" rel="#L2258">2258</span>
<span id="L2259" rel="#L2259">2259</span>
<span id="L2260" rel="#L2260">2260</span>
<span id="L2261" rel="#L2261">2261</span>
<span id="L2262" rel="#L2262">2262</span>
<span id="L2263" rel="#L2263">2263</span>
<span id="L2264" rel="#L2264">2264</span>
<span id="L2265" rel="#L2265">2265</span>
<span id="L2266" rel="#L2266">2266</span>
<span id="L2267" rel="#L2267">2267</span>
<span id="L2268" rel="#L2268">2268</span>
<span id="L2269" rel="#L2269">2269</span>
<span id="L2270" rel="#L2270">2270</span>
<span id="L2271" rel="#L2271">2271</span>
<span id="L2272" rel="#L2272">2272</span>
<span id="L2273" rel="#L2273">2273</span>
<span id="L2274" rel="#L2274">2274</span>
<span id="L2275" rel="#L2275">2275</span>
<span id="L2276" rel="#L2276">2276</span>
<span id="L2277" rel="#L2277">2277</span>
<span id="L2278" rel="#L2278">2278</span>
<span id="L2279" rel="#L2279">2279</span>
<span id="L2280" rel="#L2280">2280</span>
<span id="L2281" rel="#L2281">2281</span>
<span id="L2282" rel="#L2282">2282</span>
<span id="L2283" rel="#L2283">2283</span>
<span id="L2284" rel="#L2284">2284</span>
<span id="L2285" rel="#L2285">2285</span>
<span id="L2286" rel="#L2286">2286</span>
<span id="L2287" rel="#L2287">2287</span>
<span id="L2288" rel="#L2288">2288</span>
<span id="L2289" rel="#L2289">2289</span>
<span id="L2290" rel="#L2290">2290</span>
<span id="L2291" rel="#L2291">2291</span>
<span id="L2292" rel="#L2292">2292</span>
<span id="L2293" rel="#L2293">2293</span>
<span id="L2294" rel="#L2294">2294</span>
<span id="L2295" rel="#L2295">2295</span>
<span id="L2296" rel="#L2296">2296</span>
<span id="L2297" rel="#L2297">2297</span>
<span id="L2298" rel="#L2298">2298</span>
<span id="L2299" rel="#L2299">2299</span>
<span id="L2300" rel="#L2300">2300</span>
<span id="L2301" rel="#L2301">2301</span>
<span id="L2302" rel="#L2302">2302</span>
<span id="L2303" rel="#L2303">2303</span>
<span id="L2304" rel="#L2304">2304</span>
<span id="L2305" rel="#L2305">2305</span>
<span id="L2306" rel="#L2306">2306</span>
<span id="L2307" rel="#L2307">2307</span>
<span id="L2308" rel="#L2308">2308</span>
<span id="L2309" rel="#L2309">2309</span>
<span id="L2310" rel="#L2310">2310</span>
<span id="L2311" rel="#L2311">2311</span>
<span id="L2312" rel="#L2312">2312</span>
<span id="L2313" rel="#L2313">2313</span>
<span id="L2314" rel="#L2314">2314</span>
<span id="L2315" rel="#L2315">2315</span>
<span id="L2316" rel="#L2316">2316</span>
<span id="L2317" rel="#L2317">2317</span>
<span id="L2318" rel="#L2318">2318</span>
<span id="L2319" rel="#L2319">2319</span>
<span id="L2320" rel="#L2320">2320</span>
<span id="L2321" rel="#L2321">2321</span>
<span id="L2322" rel="#L2322">2322</span>
<span id="L2323" rel="#L2323">2323</span>
<span id="L2324" rel="#L2324">2324</span>
<span id="L2325" rel="#L2325">2325</span>
<span id="L2326" rel="#L2326">2326</span>
<span id="L2327" rel="#L2327">2327</span>
<span id="L2328" rel="#L2328">2328</span>
<span id="L2329" rel="#L2329">2329</span>
<span id="L2330" rel="#L2330">2330</span>
<span id="L2331" rel="#L2331">2331</span>
<span id="L2332" rel="#L2332">2332</span>
<span id="L2333" rel="#L2333">2333</span>
<span id="L2334" rel="#L2334">2334</span>
<span id="L2335" rel="#L2335">2335</span>
<span id="L2336" rel="#L2336">2336</span>

            </td>
            <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><span class="sd">&quot;&quot;&quot;Create a &quot;virtual&quot; Python installation</span></div><div class='line' id='LC3'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC4'><br/></div><div class='line' id='LC5'><span class="n">__version__</span> <span class="o">=</span> <span class="s">&quot;1.12.dev1&quot;</span></div><div class='line' id='LC6'><span class="n">virtualenv_version</span> <span class="o">=</span> <span class="n">__version__</span>  <span class="c"># legacy</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'><span class="kn">import</span> <span class="nn">base64</span></div><div class='line' id='LC9'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC10'><span class="kn">import</span> <span class="nn">os</span></div><div class='line' id='LC11'><span class="kn">import</span> <span class="nn">codecs</span></div><div class='line' id='LC12'><span class="kn">import</span> <span class="nn">optparse</span></div><div class='line' id='LC13'><span class="kn">import</span> <span class="nn">re</span></div><div class='line' id='LC14'><span class="kn">import</span> <span class="nn">shutil</span></div><div class='line' id='LC15'><span class="kn">import</span> <span class="nn">logging</span></div><div class='line' id='LC16'><span class="kn">import</span> <span class="nn">tempfile</span></div><div class='line' id='LC17'><span class="kn">import</span> <span class="nn">zlib</span></div><div class='line' id='LC18'><span class="kn">import</span> <span class="nn">errno</span></div><div class='line' id='LC19'><span class="kn">import</span> <span class="nn">glob</span></div><div class='line' id='LC20'><span class="kn">import</span> <span class="nn">distutils.sysconfig</span></div><div class='line' id='LC21'><span class="kn">from</span> <span class="nn">distutils.util</span> <span class="kn">import</span> <span class="n">strtobool</span></div><div class='line' id='LC22'><span class="kn">import</span> <span class="nn">struct</span></div><div class='line' id='LC23'><span class="kn">import</span> <span class="nn">subprocess</span></div><div class='line' id='LC24'><span class="kn">import</span> <span class="nn">tarfile</span></div><div class='line' id='LC25'><br/></div><div class='line' id='LC26'><span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span> <span class="o">&lt;</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">6</span><span class="p">):</span></div><div class='line' id='LC27'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="s">&#39;ERROR: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="s">&#39;ERROR: this script requires Python 2.6 or greater.&#39;</span><span class="p">)</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">101</span><span class="p">)</span></div><div class='line' id='LC30'><br/></div><div class='line' id='LC31'><span class="k">try</span><span class="p">:</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">basestring</span></div><div class='line' id='LC33'><span class="k">except</span> <span class="ne">NameError</span><span class="p">:</span></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">basestring</span> <span class="o">=</span> <span class="nb">str</span></div><div class='line' id='LC35'><br/></div><div class='line' id='LC36'><span class="k">try</span><span class="p">:</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">ConfigParser</span></div><div class='line' id='LC38'><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">configparser</span> <span class="kn">as</span> <span class="nn">ConfigParser</span></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'><span class="n">join</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span></div><div class='line' id='LC42'><span class="n">py_version</span> <span class="o">=</span> <span class="s">&#39;python</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC43'><br/></div><div class='line' id='LC44'><span class="n">is_jython</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;java&#39;</span><span class="p">)</span></div><div class='line' id='LC45'><span class="n">is_pypy</span> <span class="o">=</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">sys</span><span class="p">,</span> <span class="s">&#39;pypy_version_info&#39;</span><span class="p">)</span></div><div class='line' id='LC46'><span class="n">is_win</span> <span class="o">=</span> <span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s">&#39;win32&#39;</span><span class="p">)</span></div><div class='line' id='LC47'><span class="n">is_cygwin</span> <span class="o">=</span> <span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s">&#39;cygwin&#39;</span><span class="p">)</span></div><div class='line' id='LC48'><span class="n">is_darwin</span> <span class="o">=</span> <span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s">&#39;darwin&#39;</span><span class="p">)</span></div><div class='line' id='LC49'><span class="n">abiflags</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">sys</span><span class="p">,</span> <span class="s">&#39;abiflags&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC50'><br/></div><div class='line' id='LC51'><span class="n">user_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">expanduser</span><span class="p">(</span><span class="s">&#39;~&#39;</span><span class="p">)</span></div><div class='line' id='LC52'><span class="k">if</span> <span class="n">is_win</span><span class="p">:</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">default_storage_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">user_dir</span><span class="p">,</span> <span class="s">&#39;virtualenv&#39;</span><span class="p">)</span></div><div class='line' id='LC54'><span class="k">else</span><span class="p">:</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">default_storage_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">user_dir</span><span class="p">,</span> <span class="s">&#39;.virtualenv&#39;</span><span class="p">)</span></div><div class='line' id='LC56'><span class="n">default_config_file</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">default_storage_dir</span><span class="p">,</span> <span class="s">&#39;virtualenv.ini&#39;</span><span class="p">)</span></div><div class='line' id='LC57'><br/></div><div class='line' id='LC58'><span class="k">if</span> <span class="n">is_pypy</span><span class="p">:</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">expected_exe</span> <span class="o">=</span> <span class="s">&#39;pypy&#39;</span></div><div class='line' id='LC60'><span class="k">elif</span> <span class="n">is_jython</span><span class="p">:</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">expected_exe</span> <span class="o">=</span> <span class="s">&#39;jython&#39;</span></div><div class='line' id='LC62'><span class="k">else</span><span class="p">:</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">expected_exe</span> <span class="o">=</span> <span class="s">&#39;python&#39;</span></div><div class='line' id='LC64'><br/></div><div class='line' id='LC65'><span class="c"># Return a mapping of version -&gt; Python executable</span></div><div class='line' id='LC66'><span class="c"># Only provided for Windows, where the information in the registry is used</span></div><div class='line' id='LC67'><span class="k">if</span> <span class="ow">not</span> <span class="n">is_win</span><span class="p">:</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_installed_pythons</span><span class="p">():</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">{}</span></div><div class='line' id='LC70'><span class="k">else</span><span class="p">:</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">winreg</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">_winreg</span> <span class="kn">as</span> <span class="nn">winreg</span></div><div class='line' id='LC75'><br/></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_installed_pythons</span><span class="p">():</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">python_core</span> <span class="o">=</span> <span class="n">winreg</span><span class="o">.</span><span class="n">CreateKey</span><span class="p">(</span><span class="n">winreg</span><span class="o">.</span><span class="n">HKEY_LOCAL_MACHINE</span><span class="p">,</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Software</span><span class="se">\\</span><span class="s">Python</span><span class="se">\\</span><span class="s">PythonCore&quot;</span><span class="p">)</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">i</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">versions</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="bp">True</span><span class="p">:</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">versions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">winreg</span><span class="o">.</span><span class="n">EnumKey</span><span class="p">(</span><span class="n">python_core</span><span class="p">,</span> <span class="n">i</span><span class="p">))</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">WindowsError</span><span class="p">:</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">exes</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">ver</span> <span class="ow">in</span> <span class="n">versions</span><span class="p">:</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">path</span> <span class="o">=</span> <span class="n">winreg</span><span class="o">.</span><span class="n">QueryValue</span><span class="p">(</span><span class="n">python_core</span><span class="p">,</span> <span class="s">&quot;</span><span class="si">%s</span><span class="se">\\</span><span class="s">InstallPath&quot;</span> <span class="o">%</span> <span class="n">ver</span><span class="p">)</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">exes</span><span class="p">[</span><span class="n">ver</span><span class="p">]</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="s">&quot;python.exe&quot;</span><span class="p">)</span></div><div class='line' id='LC91'><br/></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">winreg</span><span class="o">.</span><span class="n">CloseKey</span><span class="p">(</span><span class="n">python_core</span><span class="p">)</span></div><div class='line' id='LC93'><br/></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Add the major versions</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Sort the keys, then repeatedly update the major version entry</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Last executable (i.e., highest version) wins with this approach</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">ver</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">exes</span><span class="p">):</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">exes</span><span class="p">[</span><span class="n">ver</span><span class="p">[</span><span class="mi">0</span><span class="p">]]</span> <span class="o">=</span> <span class="n">exes</span><span class="p">[</span><span class="n">ver</span><span class="p">]</span></div><div class='line' id='LC99'><br/></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">exes</span></div><div class='line' id='LC101'><br/></div><div class='line' id='LC102'><span class="n">REQUIRED_MODULES</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;os&#39;</span><span class="p">,</span> <span class="s">&#39;posix&#39;</span><span class="p">,</span> <span class="s">&#39;posixpath&#39;</span><span class="p">,</span> <span class="s">&#39;nt&#39;</span><span class="p">,</span> <span class="s">&#39;ntpath&#39;</span><span class="p">,</span> <span class="s">&#39;genericpath&#39;</span><span class="p">,</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;fnmatch&#39;</span><span class="p">,</span> <span class="s">&#39;locale&#39;</span><span class="p">,</span> <span class="s">&#39;encodings&#39;</span><span class="p">,</span> <span class="s">&#39;codecs&#39;</span><span class="p">,</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;stat&#39;</span><span class="p">,</span> <span class="s">&#39;UserDict&#39;</span><span class="p">,</span> <span class="s">&#39;readline&#39;</span><span class="p">,</span> <span class="s">&#39;copy_reg&#39;</span><span class="p">,</span> <span class="s">&#39;types&#39;</span><span class="p">,</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;re&#39;</span><span class="p">,</span> <span class="s">&#39;sre&#39;</span><span class="p">,</span> <span class="s">&#39;sre_parse&#39;</span><span class="p">,</span> <span class="s">&#39;sre_constants&#39;</span><span class="p">,</span> <span class="s">&#39;sre_compile&#39;</span><span class="p">,</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;zlib&#39;</span><span class="p">]</span></div><div class='line' id='LC107'><br/></div><div class='line' id='LC108'><span class="n">REQUIRED_FILES</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;lib-dynload&#39;</span><span class="p">,</span> <span class="s">&#39;config&#39;</span><span class="p">]</span></div><div class='line' id='LC109'><br/></div><div class='line' id='LC110'><span class="n">majver</span><span class="p">,</span> <span class="n">minver</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span></div><div class='line' id='LC111'><span class="k">if</span> <span class="n">majver</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">minver</span> <span class="o">&gt;=</span> <span class="mi">6</span><span class="p">:</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">REQUIRED_MODULES</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="s">&#39;warnings&#39;</span><span class="p">,</span> <span class="s">&#39;linecache&#39;</span><span class="p">,</span> <span class="s">&#39;_abcoll&#39;</span><span class="p">,</span> <span class="s">&#39;abc&#39;</span><span class="p">])</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">minver</span> <span class="o">&gt;=</span> <span class="mi">7</span><span class="p">:</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">REQUIRED_MODULES</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="s">&#39;_weakrefset&#39;</span><span class="p">])</span></div><div class='line' id='LC116'><span class="k">elif</span> <span class="n">majver</span> <span class="o">==</span> <span class="mi">3</span><span class="p">:</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Some extra modules are needed for Python 3, but different ones</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># for different versions.</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">REQUIRED_MODULES</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="s">&#39;_abcoll&#39;</span><span class="p">,</span> <span class="s">&#39;warnings&#39;</span><span class="p">,</span> <span class="s">&#39;linecache&#39;</span><span class="p">,</span> <span class="s">&#39;abc&#39;</span><span class="p">,</span> <span class="s">&#39;io&#39;</span><span class="p">,</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;_weakrefset&#39;</span><span class="p">,</span> <span class="s">&#39;copyreg&#39;</span><span class="p">,</span> <span class="s">&#39;tempfile&#39;</span><span class="p">,</span> <span class="s">&#39;random&#39;</span><span class="p">,</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;__future__&#39;</span><span class="p">,</span> <span class="s">&#39;collections&#39;</span><span class="p">,</span> <span class="s">&#39;keyword&#39;</span><span class="p">,</span> <span class="s">&#39;tarfile&#39;</span><span class="p">,</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;shutil&#39;</span><span class="p">,</span> <span class="s">&#39;struct&#39;</span><span class="p">,</span> <span class="s">&#39;copy&#39;</span><span class="p">,</span> <span class="s">&#39;tokenize&#39;</span><span class="p">,</span> <span class="s">&#39;token&#39;</span><span class="p">,</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;functools&#39;</span><span class="p">,</span> <span class="s">&#39;heapq&#39;</span><span class="p">,</span> <span class="s">&#39;bisect&#39;</span><span class="p">,</span> <span class="s">&#39;weakref&#39;</span><span class="p">,</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;reprlib&#39;</span><span class="p">])</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">minver</span> <span class="o">&gt;=</span> <span class="mi">2</span><span class="p">:</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">REQUIRED_FILES</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;config-</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">majver</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">minver</span> <span class="o">&gt;=</span> <span class="mi">3</span><span class="p">:</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">sysconfig</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platdir</span> <span class="o">=</span> <span class="n">sysconfig</span><span class="o">.</span><span class="n">get_config_var</span><span class="p">(</span><span class="s">&#39;PLATDIR&#39;</span><span class="p">)</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">REQUIRED_FILES</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">platdir</span><span class="p">)</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># The whole list of 3.3 modules is reproduced below - the current</span></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># uncommented ones are required for 3.3 as of now, but more may be</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># added as 3.3 development continues.</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">REQUIRED_MODULES</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;aifc&quot;,</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;antigravity&quot;,</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;argparse&quot;,</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;ast&quot;,</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;asynchat&quot;,</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;asyncore&quot;,</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;base64&quot;</span><span class="p">,</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;bdb&quot;,</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;binhex&quot;,</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;bisect&quot;,</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;calendar&quot;,</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;cgi&quot;,</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;cgitb&quot;,</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;chunk&quot;,</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;cmd&quot;,</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;codeop&quot;,</span></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;code&quot;,</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;colorsys&quot;,</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;_compat_pickle&quot;,</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;compileall&quot;,</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;concurrent&quot;,</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;configparser&quot;,</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;contextlib&quot;,</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;cProfile&quot;,</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;crypt&quot;,</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;csv&quot;,</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;ctypes&quot;,</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;curses&quot;,</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;datetime&quot;,</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;dbm&quot;,</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;decimal&quot;,</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;difflib&quot;,</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;dis&quot;,</span></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;doctest&quot;,</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;dummy_threading&quot;,</span></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;_dummy_thread&quot;</span><span class="p">,</span></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;email&quot;,</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;filecmp&quot;,</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;fileinput&quot;,</span></div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;formatter&quot;,</span></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;fractions&quot;,</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;ftplib&quot;,</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;functools&quot;,</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;getopt&quot;,</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;getpass&quot;,</span></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;gettext&quot;,</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;glob&quot;,</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;gzip&quot;,</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;hashlib&quot;</span><span class="p">,</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;heapq&quot;,</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;hmac&quot;</span><span class="p">,</span></div><div class='line' id='LC186'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;html&quot;,</span></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;http&quot;,</span></div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;idlelib&quot;,</span></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;imaplib&quot;,</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;imghdr&quot;,</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;imp&quot;</span><span class="p">,</span></div><div class='line' id='LC192'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;importlib&quot;</span><span class="p">,</span></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;inspect&quot;,</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;json&quot;,</span></div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;lib2to3&quot;,</span></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;logging&quot;,</span></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;macpath&quot;,</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;macurl2path&quot;,</span></div><div class='line' id='LC199'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;mailbox&quot;,</span></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;mailcap&quot;,</span></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;_markupbase&quot;,</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;mimetypes&quot;,</span></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;modulefinder&quot;,</span></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;multiprocessing&quot;,</span></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;netrc&quot;,</span></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;nntplib&quot;,</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;nturl2path&quot;,</span></div><div class='line' id='LC208'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;numbers&quot;,</span></div><div class='line' id='LC209'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;opcode&quot;,</span></div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;optparse&quot;,</span></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;os2emxpath&quot;,</span></div><div class='line' id='LC212'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;pdb&quot;,</span></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;pickle&quot;,</span></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;pickletools&quot;,</span></div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;pipes&quot;,</span></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;pkgutil&quot;,</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;platform&quot;,</span></div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;plat-linux2&quot;,</span></div><div class='line' id='LC219'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;plistlib&quot;,</span></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;poplib&quot;,</span></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;pprint&quot;,</span></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;profile&quot;,</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;pstats&quot;,</span></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;pty&quot;,</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;pyclbr&quot;,</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;py_compile&quot;,</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;pydoc_data&quot;,</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;pydoc&quot;,</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;_pyio&quot;,</span></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;queue&quot;,</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;quopri&quot;,</span></div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;reprlib&quot;,</span></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;rlcompleter&quot;</span><span class="p">,</span></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;runpy&quot;,</span></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;sched&quot;,</span></div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;shelve&quot;,</span></div><div class='line' id='LC237'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;shlex&quot;,</span></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;smtpd&quot;,</span></div><div class='line' id='LC239'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;smtplib&quot;,</span></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;sndhdr&quot;,</span></div><div class='line' id='LC241'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;socket&quot;,</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;socketserver&quot;,</span></div><div class='line' id='LC243'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;sqlite3&quot;,</span></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;ssl&quot;,</span></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;stringprep&quot;,</span></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;string&quot;,</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;_strptime&quot;,</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;subprocess&quot;,</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;sunau&quot;,</span></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;symbol&quot;,</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;symtable&quot;,</span></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;sysconfig&quot;,</span></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;tabnanny&quot;,</span></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;telnetlib&quot;,</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;test&quot;,</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;textwrap&quot;,</span></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;this&quot;,</span></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;_threading_local&quot;,</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;threading&quot;,</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;timeit&quot;,</span></div><div class='line' id='LC261'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;tkinter&quot;,</span></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;tokenize&quot;,</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;token&quot;,</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;traceback&quot;,</span></div><div class='line' id='LC265'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;trace&quot;,</span></div><div class='line' id='LC266'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;tty&quot;,</span></div><div class='line' id='LC267'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;turtledemo&quot;,</span></div><div class='line' id='LC268'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;turtle&quot;,</span></div><div class='line' id='LC269'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;unittest&quot;,</span></div><div class='line' id='LC270'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;urllib&quot;,</span></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;uuid&quot;,</span></div><div class='line' id='LC272'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;uu&quot;,</span></div><div class='line' id='LC273'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;wave&quot;,</span></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;weakref&quot;,</span></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;webbrowser&quot;,</span></div><div class='line' id='LC276'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;wsgiref&quot;,</span></div><div class='line' id='LC277'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;xdrlib&quot;,</span></div><div class='line' id='LC278'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;xml&quot;,</span></div><div class='line' id='LC279'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;xmlrpc&quot;,</span></div><div class='line' id='LC280'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#&quot;zipfile&quot;,</span></div><div class='line' id='LC281'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">])</span></div><div class='line' id='LC282'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">minver</span> <span class="o">&gt;=</span> <span class="mi">4</span><span class="p">:</span></div><div class='line' id='LC283'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">REQUIRED_MODULES</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span></div><div class='line' id='LC284'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;operator&#39;</span><span class="p">,</span></div><div class='line' id='LC285'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;_collections_abc&#39;</span><span class="p">,</span></div><div class='line' id='LC286'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;_bootlocale&#39;</span><span class="p">,</span></div><div class='line' id='LC287'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">])</span></div><div class='line' id='LC288'><br/></div><div class='line' id='LC289'><span class="k">if</span> <span class="n">is_pypy</span><span class="p">:</span></div><div class='line' id='LC290'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># these are needed to correctly display the exceptions that may happen</span></div><div class='line' id='LC291'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># during the bootstrap</span></div><div class='line' id='LC292'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">REQUIRED_MODULES</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="s">&#39;traceback&#39;</span><span class="p">,</span> <span class="s">&#39;linecache&#39;</span><span class="p">])</span></div><div class='line' id='LC293'><br/></div><div class='line' id='LC294'><span class="k">class</span> <span class="nc">Logger</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC295'><br/></div><div class='line' id='LC296'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC297'><span class="sd">    Logging object for use in command-line script.  Allows ranges of</span></div><div class='line' id='LC298'><span class="sd">    levels, to avoid some redundancy of displayed information.</span></div><div class='line' id='LC299'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC300'><br/></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">DEBUG</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">DEBUG</span></div><div class='line' id='LC302'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">INFO</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">INFO</span></div><div class='line' id='LC303'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">NOTIFY</span> <span class="o">=</span> <span class="p">(</span><span class="n">logging</span><span class="o">.</span><span class="n">INFO</span><span class="o">+</span><span class="n">logging</span><span class="o">.</span><span class="n">WARN</span><span class="p">)</span><span class="o">/</span><span class="mi">2</span></div><div class='line' id='LC304'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">WARN</span> <span class="o">=</span> <span class="n">WARNING</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">WARN</span></div><div class='line' id='LC305'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ERROR</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">ERROR</span></div><div class='line' id='LC306'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">FATAL</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">FATAL</span></div><div class='line' id='LC307'><br/></div><div class='line' id='LC308'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LEVELS</span> <span class="o">=</span> <span class="p">[</span><span class="n">DEBUG</span><span class="p">,</span> <span class="n">INFO</span><span class="p">,</span> <span class="n">NOTIFY</span><span class="p">,</span> <span class="n">WARN</span><span class="p">,</span> <span class="n">ERROR</span><span class="p">,</span> <span class="n">FATAL</span><span class="p">]</span></div><div class='line' id='LC309'><br/></div><div class='line' id='LC310'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">consumers</span><span class="p">):</span></div><div class='line' id='LC311'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">consumers</span> <span class="o">=</span> <span class="n">consumers</span></div><div class='line' id='LC312'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">indent</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC313'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">in_progress</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC314'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">in_progress_hanging</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC315'><br/></div><div class='line' id='LC316'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">debug</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span></div><div class='line' id='LC317'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">DEBUG</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">)</span></div><div class='line' id='LC318'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span></div><div class='line' id='LC319'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">INFO</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">)</span></div><div class='line' id='LC320'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">notify</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span></div><div class='line' id='LC321'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">NOTIFY</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">)</span></div><div class='line' id='LC322'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">warn</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span></div><div class='line' id='LC323'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">WARN</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">)</span></div><div class='line' id='LC324'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">error</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span></div><div class='line' id='LC325'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">ERROR</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">)</span></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">fatal</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">FATAL</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">)</span></div><div class='line' id='LC328'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">level</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span></div><div class='line' id='LC329'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">args</span><span class="p">:</span></div><div class='line' id='LC330'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">kw</span><span class="p">:</span></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span></div><div class='line' id='LC332'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;You may give positional or keyword arguments, not both&quot;</span><span class="p">)</span></div><div class='line' id='LC333'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">args</span> <span class="o">=</span> <span class="n">args</span> <span class="ow">or</span> <span class="n">kw</span></div><div class='line' id='LC334'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rendered</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC335'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">consumer_level</span><span class="p">,</span> <span class="n">consumer</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">consumers</span><span class="p">:</span></div><div class='line' id='LC336'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">level_matches</span><span class="p">(</span><span class="n">level</span><span class="p">,</span> <span class="n">consumer_level</span><span class="p">):</span></div><div class='line' id='LC337'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">in_progress_hanging</span></div><div class='line' id='LC338'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ow">and</span> <span class="n">consumer</span> <span class="ow">in</span> <span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="p">,</span> <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="p">)):</span></div><div class='line' id='LC339'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">in_progress_hanging</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC340'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC341'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span></div><div class='line' id='LC342'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">rendered</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC343'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">args</span><span class="p">:</span></div><div class='line' id='LC344'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rendered</span> <span class="o">=</span> <span class="n">msg</span> <span class="o">%</span> <span class="n">args</span></div><div class='line' id='LC345'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC346'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rendered</span> <span class="o">=</span> <span class="n">msg</span></div><div class='line' id='LC347'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rendered</span> <span class="o">=</span> <span class="s">&#39; &#39;</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">indent</span> <span class="o">+</span> <span class="n">rendered</span></div><div class='line' id='LC348'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">consumer</span><span class="p">,</span> <span class="s">&#39;write&#39;</span><span class="p">):</span></div><div class='line' id='LC349'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">rendered</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC350'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC351'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer</span><span class="p">(</span><span class="n">rendered</span><span class="p">)</span></div><div class='line' id='LC352'><br/></div><div class='line' id='LC353'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">start_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg</span><span class="p">):</span></div><div class='line' id='LC354'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_progress</span><span class="p">,</span> <span class="p">(</span></div><div class='line' id='LC355'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Tried to start_progress(</span><span class="si">%r</span><span class="s">) while in_progress </span><span class="si">%r</span><span class="s">&quot;</span></div><div class='line' id='LC356'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">%</span> <span class="p">(</span><span class="n">msg</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_progress</span><span class="p">))</span></div><div class='line' id='LC357'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">level_matches</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">NOTIFY</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stdout_level</span><span class="p">()):</span></div><div class='line' id='LC358'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span></div><div class='line' id='LC359'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span></div><div class='line' id='LC360'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">in_progress_hanging</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC361'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC362'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">in_progress_hanging</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC363'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">in_progress</span> <span class="o">=</span> <span class="n">msg</span></div><div class='line' id='LC364'><br/></div><div class='line' id='LC365'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">end_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg</span><span class="o">=</span><span class="s">&#39;done.&#39;</span><span class="p">):</span></div><div class='line' id='LC366'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_progress</span><span class="p">,</span> <span class="p">(</span></div><div class='line' id='LC367'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Tried to end_progress without start_progress&quot;</span><span class="p">)</span></div><div class='line' id='LC368'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">stdout_level_matches</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">NOTIFY</span><span class="p">):</span></div><div class='line' id='LC369'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_progress_hanging</span><span class="p">:</span></div><div class='line' id='LC370'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Some message has been printed out since start_progress</span></div><div class='line' id='LC371'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;...&#39;</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_progress</span> <span class="o">+</span> <span class="n">msg</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC372'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span></div><div class='line' id='LC373'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC374'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">msg</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC375'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span></div><div class='line' id='LC376'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">in_progress</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC377'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">in_progress_hanging</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC378'><br/></div><div class='line' id='LC379'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">show_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC380'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;If we are in a progress scope, and no log messages have been</span></div><div class='line' id='LC381'><span class="sd">        shown, write out another &#39;.&#39;&quot;&quot;&quot;</span></div><div class='line' id='LC382'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_progress_hanging</span><span class="p">:</span></div><div class='line' id='LC383'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">)</span></div><div class='line' id='LC384'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span></div><div class='line' id='LC385'><br/></div><div class='line' id='LC386'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">stdout_level_matches</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">level</span><span class="p">):</span></div><div class='line' id='LC387'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns true if a message at this level will go to stdout&quot;&quot;&quot;</span></div><div class='line' id='LC388'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">level_matches</span><span class="p">(</span><span class="n">level</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stdout_level</span><span class="p">())</span></div><div class='line' id='LC389'><br/></div><div class='line' id='LC390'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_stdout_level</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC391'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the level that stdout runs at&quot;&quot;&quot;</span></div><div class='line' id='LC392'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">level</span><span class="p">,</span> <span class="n">consumer</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">consumers</span><span class="p">:</span></div><div class='line' id='LC393'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">consumer</span> <span class="ow">is</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="p">:</span></div><div class='line' id='LC394'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">level</span></div><div class='line' id='LC395'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">FATAL</span></div><div class='line' id='LC396'><br/></div><div class='line' id='LC397'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">level_matches</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">level</span><span class="p">,</span> <span class="n">consumer_level</span><span class="p">):</span></div><div class='line' id='LC398'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC399'><span class="sd">        &gt;&gt;&gt; l = Logger([])</span></div><div class='line' id='LC400'><span class="sd">        &gt;&gt;&gt; l.level_matches(3, 4)</span></div><div class='line' id='LC401'><span class="sd">        False</span></div><div class='line' id='LC402'><span class="sd">        &gt;&gt;&gt; l.level_matches(3, 2)</span></div><div class='line' id='LC403'><span class="sd">        True</span></div><div class='line' id='LC404'><span class="sd">        &gt;&gt;&gt; l.level_matches(slice(None, 3), 3)</span></div><div class='line' id='LC405'><span class="sd">        False</span></div><div class='line' id='LC406'><span class="sd">        &gt;&gt;&gt; l.level_matches(slice(None, 3), 2)</span></div><div class='line' id='LC407'><span class="sd">        True</span></div><div class='line' id='LC408'><span class="sd">        &gt;&gt;&gt; l.level_matches(slice(1, 3), 1)</span></div><div class='line' id='LC409'><span class="sd">        True</span></div><div class='line' id='LC410'><span class="sd">        &gt;&gt;&gt; l.level_matches(slice(2, 3), 1)</span></div><div class='line' id='LC411'><span class="sd">        False</span></div><div class='line' id='LC412'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC413'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">level</span><span class="p">,</span> <span class="nb">slice</span><span class="p">):</span></div><div class='line' id='LC414'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">start</span><span class="p">,</span> <span class="n">stop</span> <span class="o">=</span> <span class="n">level</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="n">level</span><span class="o">.</span><span class="n">stop</span></div><div class='line' id='LC415'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">start</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="n">start</span> <span class="o">&gt;</span> <span class="n">consumer_level</span><span class="p">:</span></div><div class='line' id='LC416'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC417'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">stop</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="n">stop</span> <span class="o">&lt;=</span> <span class="n">consumer_level</span><span class="p">:</span></div><div class='line' id='LC418'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC419'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC420'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC421'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">level</span> <span class="o">&gt;=</span> <span class="n">consumer_level</span></div><div class='line' id='LC422'><br/></div><div class='line' id='LC423'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#@classmethod</span></div><div class='line' id='LC424'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">level_for_integer</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">level</span><span class="p">):</span></div><div class='line' id='LC425'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">levels</span> <span class="o">=</span> <span class="n">cls</span><span class="o">.</span><span class="n">LEVELS</span></div><div class='line' id='LC426'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">level</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC427'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">levels</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC428'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">level</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="n">levels</span><span class="p">):</span></div><div class='line' id='LC429'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">levels</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC430'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">levels</span><span class="p">[</span><span class="n">level</span><span class="p">]</span></div><div class='line' id='LC431'><br/></div><div class='line' id='LC432'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">level_for_integer</span> <span class="o">=</span> <span class="nb">classmethod</span><span class="p">(</span><span class="n">level_for_integer</span><span class="p">)</span></div><div class='line' id='LC433'><br/></div><div class='line' id='LC434'><span class="c"># create a silent logger just to prevent this from being undefined</span></div><div class='line' id='LC435'><span class="c"># will be overridden with requested verbosity main() is called.</span></div><div class='line' id='LC436'><span class="n">logger</span> <span class="o">=</span> <span class="n">Logger</span><span class="p">([(</span><span class="n">Logger</span><span class="o">.</span><span class="n">LEVELS</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="p">)])</span></div><div class='line' id='LC437'><br/></div><div class='line' id='LC438'><span class="k">def</span> <span class="nf">mkdir</span><span class="p">(</span><span class="n">path</span><span class="p">):</span></div><div class='line' id='LC439'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">path</span><span class="p">):</span></div><div class='line' id='LC440'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Creating </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">path</span><span class="p">)</span></div><div class='line' id='LC441'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">path</span><span class="p">)</span></div><div class='line' id='LC442'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC443'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Directory </span><span class="si">%s</span><span class="s"> already exists&#39;</span><span class="p">,</span> <span class="n">path</span><span class="p">)</span></div><div class='line' id='LC444'><br/></div><div class='line' id='LC445'><span class="k">def</span> <span class="nf">copyfileordir</span><span class="p">(</span><span class="n">src</span><span class="p">,</span> <span class="n">dest</span><span class="p">,</span> <span class="n">symlink</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></div><div class='line' id='LC446'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="n">src</span><span class="p">):</span></div><div class='line' id='LC447'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">copytree</span><span class="p">(</span><span class="n">src</span><span class="p">,</span> <span class="n">dest</span><span class="p">,</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC448'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC449'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">copy2</span><span class="p">(</span><span class="n">src</span><span class="p">,</span> <span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC450'><br/></div><div class='line' id='LC451'><span class="k">def</span> <span class="nf">copyfile</span><span class="p">(</span><span class="n">src</span><span class="p">,</span> <span class="n">dest</span><span class="p">,</span> <span class="n">symlink</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></div><div class='line' id='LC452'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">src</span><span class="p">):</span></div><div class='line' id='LC453'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Some bad symlink in the src</span></div><div class='line' id='LC454'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&#39;Cannot find file </span><span class="si">%s</span><span class="s"> (bad symlink)&#39;</span><span class="p">,</span> <span class="n">src</span><span class="p">)</span></div><div class='line' id='LC455'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC456'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">dest</span><span class="p">):</span></div><div class='line' id='LC457'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;File </span><span class="si">%s</span><span class="s"> already exists&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC458'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC459'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">dest</span><span class="p">)):</span></div><div class='line' id='LC460'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Creating parent directories for </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">dest</span><span class="p">))</span></div><div class='line' id='LC461'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">dest</span><span class="p">))</span></div><div class='line' id='LC462'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">islink</span><span class="p">(</span><span class="n">src</span><span class="p">):</span></div><div class='line' id='LC463'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">srcpath</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">src</span><span class="p">)</span></div><div class='line' id='LC464'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC465'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">srcpath</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">readlink</span><span class="p">(</span><span class="n">src</span><span class="p">)</span></div><div class='line' id='LC466'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">symlink</span> <span class="ow">and</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">os</span><span class="p">,</span> <span class="s">&#39;symlink&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">is_win</span><span class="p">:</span></div><div class='line' id='LC467'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Symlinking </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC468'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC469'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">symlink</span><span class="p">(</span><span class="n">srcpath</span><span class="p">,</span> <span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC470'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="p">(</span><span class="ne">OSError</span><span class="p">,</span> <span class="ne">NotImplementedError</span><span class="p">):</span></div><div class='line' id='LC471'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Symlinking failed, copying to </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC472'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfileordir</span><span class="p">(</span><span class="n">src</span><span class="p">,</span> <span class="n">dest</span><span class="p">,</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC473'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC474'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Copying to </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC475'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfileordir</span><span class="p">(</span><span class="n">src</span><span class="p">,</span> <span class="n">dest</span><span class="p">,</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC476'><br/></div><div class='line' id='LC477'><span class="k">def</span> <span class="nf">writefile</span><span class="p">(</span><span class="n">dest</span><span class="p">,</span> <span class="n">content</span><span class="p">,</span> <span class="n">overwrite</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></div><div class='line' id='LC478'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">dest</span><span class="p">):</span></div><div class='line' id='LC479'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Writing </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC480'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">dest</span><span class="p">,</span> <span class="s">&#39;wb&#39;</span><span class="p">)</span></div><div class='line' id='LC481'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">content</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&#39;utf-8&#39;</span><span class="p">))</span></div><div class='line' id='LC482'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC483'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC484'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC485'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">dest</span><span class="p">,</span> <span class="s">&#39;rb&#39;</span><span class="p">)</span></div><div class='line' id='LC486'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">c</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span></div><div class='line' id='LC487'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC488'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">c</span> <span class="o">!=</span> <span class="n">content</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&quot;utf-8&quot;</span><span class="p">):</span></div><div class='line' id='LC489'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">overwrite</span><span class="p">:</span></div><div class='line' id='LC490'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;File </span><span class="si">%s</span><span class="s"> exists with different content; not overwriting&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC491'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC492'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Overwriting </span><span class="si">%s</span><span class="s"> with new content&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC493'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">dest</span><span class="p">,</span> <span class="s">&#39;wb&#39;</span><span class="p">)</span></div><div class='line' id='LC494'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">content</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&#39;utf-8&#39;</span><span class="p">))</span></div><div class='line' id='LC495'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC496'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC497'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Content </span><span class="si">%s</span><span class="s"> already in place&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC498'><br/></div><div class='line' id='LC499'><span class="k">def</span> <span class="nf">rmtree</span><span class="p">(</span><span class="nb">dir</span><span class="p">):</span></div><div class='line' id='LC500'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="nb">dir</span><span class="p">):</span></div><div class='line' id='LC501'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Deleting tree </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">,</span> <span class="nb">dir</span><span class="p">)</span></div><div class='line' id='LC502'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">rmtree</span><span class="p">(</span><span class="nb">dir</span><span class="p">)</span></div><div class='line' id='LC503'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC504'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Do not need to delete </span><span class="si">%s</span><span class="s">; already gone&#39;</span><span class="p">,</span> <span class="nb">dir</span><span class="p">)</span></div><div class='line' id='LC505'><br/></div><div class='line' id='LC506'><span class="k">def</span> <span class="nf">make_exe</span><span class="p">(</span><span class="n">fn</span><span class="p">):</span></div><div class='line' id='LC507'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">os</span><span class="p">,</span> <span class="s">&#39;chmod&#39;</span><span class="p">):</span></div><div class='line' id='LC508'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">oldmode</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="n">fn</span><span class="p">)</span><span class="o">.</span><span class="n">st_mode</span> <span class="o">&amp;</span> <span class="mh">0xFFF</span> <span class="c"># 0o7777</span></div><div class='line' id='LC509'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">newmode</span> <span class="o">=</span> <span class="p">(</span><span class="n">oldmode</span> <span class="o">|</span> <span class="mh">0x16D</span><span class="p">)</span> <span class="o">&amp;</span> <span class="mh">0xFFF</span> <span class="c"># 0o555, 0o7777</span></div><div class='line' id='LC510'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">chmod</span><span class="p">(</span><span class="n">fn</span><span class="p">,</span> <span class="n">newmode</span><span class="p">)</span></div><div class='line' id='LC511'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Changed mode of </span><span class="si">%s</span><span class="s"> to </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">fn</span><span class="p">,</span> <span class="nb">oct</span><span class="p">(</span><span class="n">newmode</span><span class="p">))</span></div><div class='line' id='LC512'><br/></div><div class='line' id='LC513'><span class="k">def</span> <span class="nf">_find_file</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">dirs</span><span class="p">):</span></div><div class='line' id='LC514'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="nb">dir</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">dirs</span><span class="p">):</span></div><div class='line' id='LC515'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span> <span class="o">=</span> <span class="n">glob</span><span class="o">.</span><span class="n">glob</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">dir</span><span class="p">,</span> <span class="n">filename</span><span class="p">))</span></div><div class='line' id='LC516'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">files</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="n">files</span><span class="p">[</span><span class="mi">0</span><span class="p">]):</span></div><div class='line' id='LC517'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span><span class="p">,</span> <span class="n">files</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC518'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span><span class="p">,</span> <span class="n">filename</span></div><div class='line' id='LC519'><br/></div><div class='line' id='LC520'><span class="k">def</span> <span class="nf">file_search_dirs</span><span class="p">():</span></div><div class='line' id='LC521'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">here</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">__file__</span><span class="p">))</span></div><div class='line' id='LC522'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dirs</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;.&#39;</span><span class="p">,</span> <span class="n">here</span><span class="p">,</span></div><div class='line' id='LC523'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">join</span><span class="p">(</span><span class="n">here</span><span class="p">,</span> <span class="s">&#39;virtualenv_support&#39;</span><span class="p">)]</span></div><div class='line' id='LC524'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">__file__</span><span class="p">))[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&#39;virtualenv&#39;</span><span class="p">:</span></div><div class='line' id='LC525'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Probably some boot script; just in case virtualenv is installed...</span></div><div class='line' id='LC526'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC527'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">virtualenv</span></div><div class='line' id='LC528'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div><div class='line' id='LC529'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC530'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC531'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dirs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">virtualenv</span><span class="o">.</span><span class="n">__file__</span><span class="p">),</span> <span class="s">&#39;virtualenv_support&#39;</span><span class="p">))</span></div><div class='line' id='LC532'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">d</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">dirs</span> <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="n">d</span><span class="p">)]</span></div><div class='line' id='LC533'><br/></div><div class='line' id='LC534'><br/></div><div class='line' id='LC535'><span class="k">class</span> <span class="nc">UpdatingDefaultsHelpFormatter</span><span class="p">(</span><span class="n">optparse</span><span class="o">.</span><span class="n">IndentedHelpFormatter</span><span class="p">):</span></div><div class='line' id='LC536'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC537'><span class="sd">    Custom help formatter for use in ConfigOptionParser that updates</span></div><div class='line' id='LC538'><span class="sd">    the defaults before expanding them, allowing them to show up correctly</span></div><div class='line' id='LC539'><span class="sd">    in the help listing</span></div><div class='line' id='LC540'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC541'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">expand_default</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">option</span><span class="p">):</span></div><div class='line' id='LC542'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC543'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">parser</span><span class="o">.</span><span class="n">update_defaults</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">parser</span><span class="o">.</span><span class="n">defaults</span><span class="p">)</span></div><div class='line' id='LC544'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">optparse</span><span class="o">.</span><span class="n">IndentedHelpFormatter</span><span class="o">.</span><span class="n">expand_default</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">option</span><span class="p">)</span></div><div class='line' id='LC545'><br/></div><div class='line' id='LC546'><br/></div><div class='line' id='LC547'><span class="k">class</span> <span class="nc">ConfigOptionParser</span><span class="p">(</span><span class="n">optparse</span><span class="o">.</span><span class="n">OptionParser</span><span class="p">):</span></div><div class='line' id='LC548'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC549'><span class="sd">    Custom option parser which updates its defaults by checking the</span></div><div class='line' id='LC550'><span class="sd">    configuration files and environmental variables</span></div><div class='line' id='LC551'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC552'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span></div><div class='line' id='LC553'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">config</span> <span class="o">=</span> <span class="n">ConfigParser</span><span class="o">.</span><span class="n">RawConfigParser</span><span class="p">()</span></div><div class='line' id='LC554'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">files</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_config_files</span><span class="p">()</span></div><div class='line' id='LC555'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">files</span><span class="p">)</span></div><div class='line' id='LC556'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">optparse</span><span class="o">.</span><span class="n">OptionParser</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span></div><div class='line' id='LC557'><br/></div><div class='line' id='LC558'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_config_files</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC559'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">config_file</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;VIRTUALENV_CONFIG_FILE&#39;</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC560'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">config_file</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">config_file</span><span class="p">):</span></div><div class='line' id='LC561'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">config_file</span><span class="p">]</span></div><div class='line' id='LC562'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">default_config_file</span><span class="p">]</span></div><div class='line' id='LC563'><br/></div><div class='line' id='LC564'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">update_defaults</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">defaults</span><span class="p">):</span></div><div class='line' id='LC565'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC566'><span class="sd">        Updates the given defaults with values from the config files and</span></div><div class='line' id='LC567'><span class="sd">        the environ. Does a little special handling for certain types of</span></div><div class='line' id='LC568'><span class="sd">        options (lists).</span></div><div class='line' id='LC569'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC570'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Then go and look for the other sources of configuration:</span></div><div class='line' id='LC571'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">config</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC572'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># 1. config files</span></div><div class='line' id='LC573'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">config</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="nb">dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_config_section</span><span class="p">(</span><span class="s">&#39;virtualenv&#39;</span><span class="p">)))</span></div><div class='line' id='LC574'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># 2. environmental variables</span></div><div class='line' id='LC575'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">config</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="nb">dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_environ_vars</span><span class="p">()))</span></div><div class='line' id='LC576'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Then set the options with those values</span></div><div class='line' id='LC577'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">config</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></div><div class='line' id='LC578'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">key</span> <span class="o">=</span> <span class="n">key</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;_&#39;</span><span class="p">,</span> <span class="s">&#39;-&#39;</span><span class="p">)</span></div><div class='line' id='LC579'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;--&#39;</span><span class="p">):</span></div><div class='line' id='LC580'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">key</span> <span class="o">=</span> <span class="s">&#39;--</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">key</span>  <span class="c"># only prefer long opts</span></div><div class='line' id='LC581'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">option</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_option</span><span class="p">(</span><span class="n">key</span><span class="p">)</span></div><div class='line' id='LC582'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">option</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC583'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># ignore empty values</span></div><div class='line' id='LC584'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">val</span><span class="p">:</span></div><div class='line' id='LC585'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC586'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># handle multiline configs</span></div><div class='line' id='LC587'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">option</span><span class="o">.</span><span class="n">action</span> <span class="o">==</span> <span class="s">&#39;append&#39;</span><span class="p">:</span></div><div class='line' id='LC588'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">val</span> <span class="o">=</span> <span class="n">val</span><span class="o">.</span><span class="n">split</span><span class="p">()</span></div><div class='line' id='LC589'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC590'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">option</span><span class="o">.</span><span class="n">nargs</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC591'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">option</span><span class="o">.</span><span class="n">action</span> <span class="o">==</span> <span class="s">&#39;store_false&#39;</span><span class="p">:</span></div><div class='line' id='LC592'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">val</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">strtobool</span><span class="p">(</span><span class="n">val</span><span class="p">)</span></div><div class='line' id='LC593'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">option</span><span class="o">.</span><span class="n">action</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span> <span class="s">&#39;count&#39;</span><span class="p">):</span></div><div class='line' id='LC594'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">val</span> <span class="o">=</span> <span class="n">strtobool</span><span class="p">(</span><span class="n">val</span><span class="p">)</span></div><div class='line' id='LC595'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC596'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">val</span> <span class="o">=</span> <span class="n">option</span><span class="o">.</span><span class="n">convert_value</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">val</span><span class="p">)</span></div><div class='line' id='LC597'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="n">optparse</span><span class="o">.</span><span class="n">OptionValueError</span><span class="p">:</span></div><div class='line' id='LC598'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">e</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC599'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="s">&quot;An error occured during configuration: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">e</span><span class="p">)</span></div><div class='line' id='LC600'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span></div><div class='line' id='LC601'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">defaults</span><span class="p">[</span><span class="n">option</span><span class="o">.</span><span class="n">dest</span><span class="p">]</span> <span class="o">=</span> <span class="n">val</span></div><div class='line' id='LC602'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">defaults</span></div><div class='line' id='LC603'><br/></div><div class='line' id='LC604'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_config_section</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span></div><div class='line' id='LC605'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC606'><span class="sd">        Get a section of a configuration</span></div><div class='line' id='LC607'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC608'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">has_section</span><span class="p">(</span><span class="n">name</span><span class="p">):</span></div><div class='line' id='LC609'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">items</span><span class="p">(</span><span class="n">name</span><span class="p">)</span></div><div class='line' id='LC610'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[]</span></div><div class='line' id='LC611'><br/></div><div class='line' id='LC612'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_environ_vars</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prefix</span><span class="o">=</span><span class="s">&#39;VIRTUALENV_&#39;</span><span class="p">):</span></div><div class='line' id='LC613'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC614'><span class="sd">        Returns a generator with all environmental vars with prefix VIRTUALENV</span></div><div class='line' id='LC615'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC616'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></div><div class='line' id='LC617'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">prefix</span><span class="p">):</span></div><div class='line' id='LC618'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">yield</span> <span class="p">(</span><span class="n">key</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">lower</span><span class="p">(),</span> <span class="n">val</span><span class="p">)</span></div><div class='line' id='LC619'><br/></div><div class='line' id='LC620'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_default_values</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC621'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC622'><span class="sd">        Overridding to make updating the defaults after instantiation of</span></div><div class='line' id='LC623'><span class="sd">        the option parser possible, update_defaults() does the dirty work.</span></div><div class='line' id='LC624'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC625'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_default_values</span><span class="p">:</span></div><div class='line' id='LC626'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Old, pre-Optik 1.5 behaviour.</span></div><div class='line' id='LC627'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">optparse</span><span class="o">.</span><span class="n">Values</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">defaults</span><span class="p">)</span></div><div class='line' id='LC628'><br/></div><div class='line' id='LC629'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">defaults</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">update_defaults</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">defaults</span><span class="o">.</span><span class="n">copy</span><span class="p">())</span>  <span class="c"># ours</span></div><div class='line' id='LC630'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">option</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_all_options</span><span class="p">():</span></div><div class='line' id='LC631'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">default</span> <span class="o">=</span> <span class="n">defaults</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">option</span><span class="o">.</span><span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC632'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">default</span><span class="p">,</span> <span class="nb">basestring</span><span class="p">):</span></div><div class='line' id='LC633'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">opt_str</span> <span class="o">=</span> <span class="n">option</span><span class="o">.</span><span class="n">get_opt_string</span><span class="p">()</span></div><div class='line' id='LC634'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">defaults</span><span class="p">[</span><span class="n">option</span><span class="o">.</span><span class="n">dest</span><span class="p">]</span> <span class="o">=</span> <span class="n">option</span><span class="o">.</span><span class="n">check_value</span><span class="p">(</span><span class="n">opt_str</span><span class="p">,</span> <span class="n">default</span><span class="p">)</span></div><div class='line' id='LC635'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">optparse</span><span class="o">.</span><span class="n">Values</span><span class="p">(</span><span class="n">defaults</span><span class="p">)</span></div><div class='line' id='LC636'><br/></div><div class='line' id='LC637'><br/></div><div class='line' id='LC638'><span class="k">def</span> <span class="nf">main</span><span class="p">():</span></div><div class='line' id='LC639'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span> <span class="o">=</span> <span class="n">ConfigOptionParser</span><span class="p">(</span></div><div class='line' id='LC640'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version</span><span class="o">=</span><span class="n">virtualenv_version</span><span class="p">,</span></div><div class='line' id='LC641'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">usage</span><span class="o">=</span><span class="s">&quot;%prog [OPTIONS] DEST_DIR&quot;</span><span class="p">,</span></div><div class='line' id='LC642'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">formatter</span><span class="o">=</span><span class="n">UpdatingDefaultsHelpFormatter</span><span class="p">())</span></div><div class='line' id='LC643'><br/></div><div class='line' id='LC644'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC645'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;-v&#39;</span><span class="p">,</span> <span class="s">&#39;--verbose&#39;</span><span class="p">,</span></div><div class='line' id='LC646'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&#39;count&#39;</span><span class="p">,</span></div><div class='line' id='LC647'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;verbose&#39;</span><span class="p">,</span></div><div class='line' id='LC648'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">default</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span></div><div class='line' id='LC649'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&quot;Increase verbosity.&quot;</span><span class="p">)</span></div><div class='line' id='LC650'><br/></div><div class='line' id='LC651'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC652'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;-q&#39;</span><span class="p">,</span> <span class="s">&#39;--quiet&#39;</span><span class="p">,</span></div><div class='line' id='LC653'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&#39;count&#39;</span><span class="p">,</span></div><div class='line' id='LC654'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;quiet&#39;</span><span class="p">,</span></div><div class='line' id='LC655'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">default</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span></div><div class='line' id='LC656'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;Decrease verbosity.&#39;</span><span class="p">)</span></div><div class='line' id='LC657'><br/></div><div class='line' id='LC658'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC659'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;-p&#39;</span><span class="p">,</span> <span class="s">&#39;--python&#39;</span><span class="p">,</span></div><div class='line' id='LC660'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;python&#39;</span><span class="p">,</span></div><div class='line' id='LC661'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">metavar</span><span class="o">=</span><span class="s">&#39;PYTHON_EXE&#39;</span><span class="p">,</span></div><div class='line' id='LC662'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;The Python interpreter to use, e.g., --python=python2.5 will use the python2.5 &#39;</span></div><div class='line' id='LC663'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;interpreter to create the new environment.  The default is the interpreter that &#39;</span></div><div class='line' id='LC664'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;virtualenv was installed with (</span><span class="si">%s</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">)</span></div><div class='line' id='LC665'><br/></div><div class='line' id='LC666'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC667'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;--clear&#39;</span><span class="p">,</span></div><div class='line' id='LC668'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;clear&#39;</span><span class="p">,</span></div><div class='line' id='LC669'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span></div><div class='line' id='LC670'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&quot;Clear out the non-root install and start from scratch.&quot;</span><span class="p">)</span></div><div class='line' id='LC671'><br/></div><div class='line' id='LC672'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">set_defaults</span><span class="p">(</span><span class="n">system_site_packages</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC673'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC674'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;--no-site-packages&#39;</span><span class="p">,</span></div><div class='line' id='LC675'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;system_site_packages&#39;</span><span class="p">,</span></div><div class='line' id='LC676'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&#39;store_false&#39;</span><span class="p">,</span></div><div class='line' id='LC677'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&quot;DEPRECATED. Retained only for backward compatibility. &quot;</span></div><div class='line' id='LC678'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Not having access to global site-packages is now the default behavior.&quot;</span><span class="p">)</span></div><div class='line' id='LC679'><br/></div><div class='line' id='LC680'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC681'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;--system-site-packages&#39;</span><span class="p">,</span></div><div class='line' id='LC682'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;system_site_packages&#39;</span><span class="p">,</span></div><div class='line' id='LC683'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span></div><div class='line' id='LC684'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&quot;Give the virtual environment access to the global site-packages.&quot;</span><span class="p">)</span></div><div class='line' id='LC685'><br/></div><div class='line' id='LC686'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC687'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;--always-copy&#39;</span><span class="p">,</span></div><div class='line' id='LC688'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;symlink&#39;</span><span class="p">,</span></div><div class='line' id='LC689'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&#39;store_false&#39;</span><span class="p">,</span></div><div class='line' id='LC690'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">default</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span></div><div class='line' id='LC691'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&quot;Always copy files rather than symlinking.&quot;</span><span class="p">)</span></div><div class='line' id='LC692'><br/></div><div class='line' id='LC693'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC694'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;--unzip-setuptools&#39;</span><span class="p">,</span></div><div class='line' id='LC695'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;unzip_setuptools&#39;</span><span class="p">,</span></div><div class='line' id='LC696'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span></div><div class='line' id='LC697'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&quot;Unzip Setuptools when installing it.&quot;</span><span class="p">)</span></div><div class='line' id='LC698'><br/></div><div class='line' id='LC699'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC700'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;--relocatable&#39;</span><span class="p">,</span></div><div class='line' id='LC701'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;relocatable&#39;</span><span class="p">,</span></div><div class='line' id='LC702'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span></div><div class='line' id='LC703'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;Make an EXISTING virtualenv environment relocatable. &#39;</span></div><div class='line' id='LC704'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;This fixes up scripts and makes all .pth files relative.&#39;</span><span class="p">)</span></div><div class='line' id='LC705'><br/></div><div class='line' id='LC706'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC707'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;--no-setuptools&#39;</span><span class="p">,</span></div><div class='line' id='LC708'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;no_setuptools&#39;</span><span class="p">,</span></div><div class='line' id='LC709'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span></div><div class='line' id='LC710'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;Do not install setuptools (or pip) in the new virtualenv.&#39;</span><span class="p">)</span></div><div class='line' id='LC711'><br/></div><div class='line' id='LC712'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC713'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;--no-pip&#39;</span><span class="p">,</span></div><div class='line' id='LC714'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;no_pip&#39;</span><span class="p">,</span></div><div class='line' id='LC715'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span></div><div class='line' id='LC716'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;Do not install pip in the new virtualenv.&#39;</span><span class="p">)</span></div><div class='line' id='LC717'><br/></div><div class='line' id='LC718'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">default_search_dirs</span> <span class="o">=</span> <span class="n">file_search_dirs</span><span class="p">()</span></div><div class='line' id='LC719'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC720'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;--extra-search-dir&#39;</span><span class="p">,</span></div><div class='line' id='LC721'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&quot;search_dirs&quot;</span><span class="p">,</span></div><div class='line' id='LC722'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&quot;append&quot;</span><span class="p">,</span></div><div class='line' id='LC723'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">metavar</span><span class="o">=</span><span class="s">&#39;DIR&#39;</span><span class="p">,</span></div><div class='line' id='LC724'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">default</span><span class="o">=</span><span class="n">default_search_dirs</span><span class="p">,</span></div><div class='line' id='LC725'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&quot;Directory to look for setuptools/pip distributions in. &quot;</span></div><div class='line' id='LC726'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;This option can be used multiple times.&quot;</span><span class="p">)</span></div><div class='line' id='LC727'><br/></div><div class='line' id='LC728'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC729'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;--never-download&#39;</span><span class="p">,</span></div><div class='line' id='LC730'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&quot;never_download&quot;</span><span class="p">,</span></div><div class='line' id='LC731'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&quot;store_true&quot;</span><span class="p">,</span></div><div class='line' id='LC732'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">default</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span></div><div class='line' id='LC733'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&quot;DEPRECATED. Retained only for backward compatibility. This option has no effect. &quot;</span></div><div class='line' id='LC734'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Virtualenv never downloads pip or setuptools.&quot;</span><span class="p">)</span></div><div class='line' id='LC735'><br/></div><div class='line' id='LC736'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC737'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;--prompt&#39;</span><span class="p">,</span></div><div class='line' id='LC738'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;prompt&#39;</span><span class="p">,</span></div><div class='line' id='LC739'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;Provides an alternative prompt prefix for this environment.&#39;</span><span class="p">)</span></div><div class='line' id='LC740'><br/></div><div class='line' id='LC741'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC742'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;--setuptools&#39;</span><span class="p">,</span></div><div class='line' id='LC743'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;setuptools&#39;</span><span class="p">,</span></div><div class='line' id='LC744'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span></div><div class='line' id='LC745'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&quot;DEPRECATED. Retained only for backward compatibility. This option has no effect.&quot;</span><span class="p">)</span></div><div class='line' id='LC746'><br/></div><div class='line' id='LC747'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span></div><div class='line' id='LC748'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;--distribute&#39;</span><span class="p">,</span></div><div class='line' id='LC749'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;distribute&#39;</span><span class="p">,</span></div><div class='line' id='LC750'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span></div><div class='line' id='LC751'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&quot;DEPRECATED. Retained only for backward compatibility. This option has no effect.&quot;</span><span class="p">)</span></div><div class='line' id='LC752'><br/></div><div class='line' id='LC753'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;extend_parser&#39;</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">():</span></div><div class='line' id='LC754'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">extend_parser</span><span class="p">(</span><span class="n">parser</span><span class="p">)</span></div><div class='line' id='LC755'><br/></div><div class='line' id='LC756'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">options</span><span class="p">,</span> <span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span></div><div class='line' id='LC757'><br/></div><div class='line' id='LC758'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">logger</span></div><div class='line' id='LC759'><br/></div><div class='line' id='LC760'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;adjust_options&#39;</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">():</span></div><div class='line' id='LC761'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">adjust_options</span><span class="p">(</span><span class="n">options</span><span class="p">,</span> <span class="n">args</span><span class="p">)</span></div><div class='line' id='LC762'><br/></div><div class='line' id='LC763'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">verbosity</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">verbose</span> <span class="o">-</span> <span class="n">options</span><span class="o">.</span><span class="n">quiet</span></div><div class='line' id='LC764'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span> <span class="o">=</span> <span class="n">Logger</span><span class="p">([(</span><span class="n">Logger</span><span class="o">.</span><span class="n">level_for_integer</span><span class="p">(</span><span class="mi">2</span> <span class="o">-</span> <span class="n">verbosity</span><span class="p">),</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="p">)])</span></div><div class='line' id='LC765'><br/></div><div class='line' id='LC766'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">python</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;VIRTUALENV_INTERPRETER_RUNNING&#39;</span><span class="p">):</span></div><div class='line' id='LC767'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">env</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span></div><div class='line' id='LC768'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">interpreter</span> <span class="o">=</span> <span class="n">resolve_interpreter</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">python</span><span class="p">)</span></div><div class='line' id='LC769'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">interpreter</span> <span class="o">==</span> <span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">:</span></div><div class='line' id='LC770'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&#39;Already using interpreter </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">interpreter</span><span class="p">)</span></div><div class='line' id='LC771'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC772'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Running virtualenv with interpreter </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">interpreter</span><span class="p">)</span></div><div class='line' id='LC773'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">env</span><span class="p">[</span><span class="s">&#39;VIRTUALENV_INTERPRETER_RUNNING&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;true&#39;</span></div><div class='line' id='LC774'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">file</span> <span class="o">=</span> <span class="n">__file__</span></div><div class='line' id='LC775'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">file</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;.pyc&#39;</span><span class="p">):</span></div><div class='line' id='LC776'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">file</span> <span class="o">=</span> <span class="nb">file</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC777'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">popen</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">([</span><span class="n">interpreter</span><span class="p">,</span> <span class="nb">file</span><span class="p">]</span> <span class="o">+</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">env</span><span class="o">=</span><span class="n">env</span><span class="p">)</span></div><div class='line' id='LC778'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">SystemExit</span><span class="p">(</span><span class="n">popen</span><span class="o">.</span><span class="n">wait</span><span class="p">())</span></div><div class='line' id='LC779'><br/></div><div class='line' id='LC780'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">args</span><span class="p">:</span></div><div class='line' id='LC781'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="s">&#39;You must provide a DEST_DIR&#39;</span><span class="p">)</span></div><div class='line' id='LC782'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">print_help</span><span class="p">()</span></div><div class='line' id='LC783'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span></div><div class='line' id='LC784'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC785'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="s">&#39;There must be only one argument: DEST_DIR (you gave </span><span class="si">%s</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="p">(</span></div><div class='line' id='LC786'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">args</span><span class="p">)))</span></div><div class='line' id='LC787'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">print_help</span><span class="p">()</span></div><div class='line' id='LC788'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span></div><div class='line' id='LC789'><br/></div><div class='line' id='LC790'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">home_dir</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC791'><br/></div><div class='line' id='LC792'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;WORKING_ENV&#39;</span><span class="p">):</span></div><div class='line' id='LC793'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span><span class="s">&#39;ERROR: you cannot run virtualenv while in a workingenv&#39;</span><span class="p">)</span></div><div class='line' id='LC794'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span><span class="s">&#39;Please deactivate your workingenv, then re-run this script&#39;</span><span class="p">)</span></div><div class='line' id='LC795'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span></div><div class='line' id='LC796'><br/></div><div class='line' id='LC797'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;PYTHONHOME&#39;</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">:</span></div><div class='line' id='LC798'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&#39;PYTHONHOME is set.  You *must* activate the virtualenv before using it&#39;</span><span class="p">)</span></div><div class='line' id='LC799'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">del</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s">&#39;PYTHONHOME&#39;</span><span class="p">]</span></div><div class='line' id='LC800'><br/></div><div class='line' id='LC801'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">relocatable</span><span class="p">:</span></div><div class='line' id='LC802'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">make_environment_relocatable</span><span class="p">(</span><span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC803'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC804'><br/></div><div class='line' id='LC805'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">options</span><span class="o">.</span><span class="n">never_download</span><span class="p">:</span></div><div class='line' id='LC806'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&#39;The --never-download option is for backward compatibility only.&#39;</span><span class="p">)</span></div><div class='line' id='LC807'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&#39;Setting it to false is no longer supported, and will be ignored.&#39;</span><span class="p">)</span></div><div class='line' id='LC808'><br/></div><div class='line' id='LC809'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">create_environment</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span></div><div class='line' id='LC810'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">site_packages</span><span class="o">=</span><span class="n">options</span><span class="o">.</span><span class="n">system_site_packages</span><span class="p">,</span></div><div class='line' id='LC811'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">clear</span><span class="o">=</span><span class="n">options</span><span class="o">.</span><span class="n">clear</span><span class="p">,</span></div><div class='line' id='LC812'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">unzip_setuptools</span><span class="o">=</span><span class="n">options</span><span class="o">.</span><span class="n">unzip_setuptools</span><span class="p">,</span></div><div class='line' id='LC813'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prompt</span><span class="o">=</span><span class="n">options</span><span class="o">.</span><span class="n">prompt</span><span class="p">,</span></div><div class='line' id='LC814'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">search_dirs</span><span class="o">=</span><span class="n">options</span><span class="o">.</span><span class="n">search_dirs</span><span class="p">,</span></div><div class='line' id='LC815'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">never_download</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span></div><div class='line' id='LC816'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">no_setuptools</span><span class="o">=</span><span class="n">options</span><span class="o">.</span><span class="n">no_setuptools</span><span class="p">,</span></div><div class='line' id='LC817'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">no_pip</span><span class="o">=</span><span class="n">options</span><span class="o">.</span><span class="n">no_pip</span><span class="p">,</span></div><div class='line' id='LC818'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">symlink</span><span class="o">=</span><span class="n">options</span><span class="o">.</span><span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC819'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;after_install&#39;</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">():</span></div><div class='line' id='LC820'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">after_install</span><span class="p">(</span><span class="n">options</span><span class="p">,</span> <span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC821'><br/></div><div class='line' id='LC822'><span class="k">def</span> <span class="nf">call_subprocess</span><span class="p">(</span><span class="n">cmd</span><span class="p">,</span> <span class="n">show_stdout</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span></div><div class='line' id='LC823'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filter_stdout</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">cwd</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC824'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">raise_on_returncode</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">extra_env</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC825'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">remove_from_env</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC826'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cmd_parts</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC827'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">cmd</span><span class="p">:</span></div><div class='line' id='LC828'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">part</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">45</span><span class="p">:</span></div><div class='line' id='LC829'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">part</span> <span class="o">=</span> <span class="n">part</span><span class="p">[:</span><span class="mi">20</span><span class="p">]</span><span class="o">+</span><span class="s">&quot;...&quot;</span><span class="o">+</span><span class="n">part</span><span class="p">[</span><span class="o">-</span><span class="mi">20</span><span class="p">:]</span></div><div class='line' id='LC830'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39; &#39;</span> <span class="ow">in</span> <span class="n">part</span> <span class="ow">or</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span> <span class="ow">in</span> <span class="n">part</span> <span class="ow">or</span> <span class="s">&#39;&quot;&#39;</span> <span class="ow">in</span> <span class="n">part</span> <span class="ow">or</span> <span class="s">&quot;&#39;&quot;</span> <span class="ow">in</span> <span class="n">part</span><span class="p">:</span></div><div class='line' id='LC831'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">part</span> <span class="o">=</span> <span class="s">&#39;&quot;</span><span class="si">%s</span><span class="s">&quot;&#39;</span> <span class="o">%</span> <span class="n">part</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;&quot;&#39;</span><span class="p">,</span> <span class="s">&#39;</span><span class="se">\\</span><span class="s">&quot;&#39;</span><span class="p">)</span></div><div class='line' id='LC832'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="s">&#39;decode&#39;</span><span class="p">):</span></div><div class='line' id='LC833'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC834'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">part</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getdefaultencoding</span><span class="p">())</span></div><div class='line' id='LC835'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">UnicodeDecodeError</span><span class="p">:</span></div><div class='line' id='LC836'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">part</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getfilesystemencoding</span><span class="p">())</span></div><div class='line' id='LC837'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cmd_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">part</span><span class="p">)</span></div><div class='line' id='LC838'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cmd_desc</span> <span class="o">=</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">cmd_parts</span><span class="p">)</span></div><div class='line' id='LC839'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">show_stdout</span><span class="p">:</span></div><div class='line' id='LC840'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stdout</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC841'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC842'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stdout</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span></div><div class='line' id='LC843'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&quot;Running command </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">cmd_desc</span><span class="p">)</span></div><div class='line' id='LC844'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">extra_env</span> <span class="ow">or</span> <span class="n">remove_from_env</span><span class="p">:</span></div><div class='line' id='LC845'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">env</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span></div><div class='line' id='LC846'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">extra_env</span><span class="p">:</span></div><div class='line' id='LC847'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">env</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_env</span><span class="p">)</span></div><div class='line' id='LC848'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">remove_from_env</span><span class="p">:</span></div><div class='line' id='LC849'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">varname</span> <span class="ow">in</span> <span class="n">remove_from_env</span><span class="p">:</span></div><div class='line' id='LC850'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">env</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">varname</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></div><div class='line' id='LC851'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC852'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">env</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC853'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC854'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">proc</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">(</span></div><div class='line' id='LC855'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cmd</span><span class="p">,</span> <span class="n">stderr</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">STDOUT</span><span class="p">,</span> <span class="n">stdin</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">stdout</span><span class="o">=</span><span class="n">stdout</span><span class="p">,</span></div><div class='line' id='LC856'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cwd</span><span class="o">=</span><span class="n">cwd</span><span class="p">,</span> <span class="n">env</span><span class="o">=</span><span class="n">env</span><span class="p">)</span></div><div class='line' id='LC857'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span></div><div class='line' id='LC858'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">e</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC859'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span></div><div class='line' id='LC860'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Error </span><span class="si">%s</span><span class="s"> while executing command </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">e</span><span class="p">,</span> <span class="n">cmd_desc</span><span class="p">))</span></div><div class='line' id='LC861'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span></div><div class='line' id='LC862'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">all_output</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC863'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">stdout</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC864'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stdout</span> <span class="o">=</span> <span class="n">proc</span><span class="o">.</span><span class="n">stdout</span></div><div class='line' id='LC865'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">encoding</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">getdefaultencoding</span><span class="p">()</span></div><div class='line' id='LC866'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fs_encoding</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">getfilesystemencoding</span><span class="p">()</span></div><div class='line' id='LC867'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC868'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">line</span> <span class="o">=</span> <span class="n">stdout</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span></div><div class='line' id='LC869'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC870'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">line</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="p">)</span></div><div class='line' id='LC871'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">UnicodeDecodeError</span><span class="p">:</span></div><div class='line' id='LC872'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">line</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">fs_encoding</span><span class="p">)</span></div><div class='line' id='LC873'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">line</span><span class="p">:</span></div><div class='line' id='LC874'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC875'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">line</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">rstrip</span><span class="p">()</span></div><div class='line' id='LC876'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">all_output</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="p">)</span></div><div class='line' id='LC877'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">filter_stdout</span><span class="p">:</span></div><div class='line' id='LC878'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">level</span> <span class="o">=</span> <span class="n">filter_stdout</span><span class="p">(</span><span class="n">line</span><span class="p">)</span></div><div class='line' id='LC879'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">level</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span></div><div class='line' id='LC880'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">level</span><span class="p">,</span> <span class="n">line</span> <span class="o">=</span> <span class="n">level</span></div><div class='line' id='LC881'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="n">level</span><span class="p">,</span> <span class="n">line</span><span class="p">)</span></div><div class='line' id='LC882'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">logger</span><span class="o">.</span><span class="n">stdout_level_matches</span><span class="p">(</span><span class="n">level</span><span class="p">):</span></div><div class='line' id='LC883'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">show_progress</span><span class="p">()</span></div><div class='line' id='LC884'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC885'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">line</span><span class="p">)</span></div><div class='line' id='LC886'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC887'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">proc</span><span class="o">.</span><span class="n">communicate</span><span class="p">()</span></div><div class='line' id='LC888'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">proc</span><span class="o">.</span><span class="n">wait</span><span class="p">()</span></div><div class='line' id='LC889'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">proc</span><span class="o">.</span><span class="n">returncode</span><span class="p">:</span></div><div class='line' id='LC890'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">raise_on_returncode</span><span class="p">:</span></div><div class='line' id='LC891'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">all_output</span><span class="p">:</span></div><div class='line' id='LC892'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Complete output from command </span><span class="si">%s</span><span class="s">:&#39;</span> <span class="o">%</span> <span class="n">cmd_desc</span><span class="p">)</span></div><div class='line' id='LC893'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">all_output</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">----------------------------------------&#39;</span><span class="p">)</span></div><div class='line' id='LC894'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">OSError</span><span class="p">(</span></div><div class='line' id='LC895'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Command </span><span class="si">%s</span><span class="s"> failed with error code </span><span class="si">%s</span><span class="s">&quot;</span></div><div class='line' id='LC896'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">%</span> <span class="p">(</span><span class="n">cmd_desc</span><span class="p">,</span> <span class="n">proc</span><span class="o">.</span><span class="n">returncode</span><span class="p">))</span></div><div class='line' id='LC897'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC898'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span></div><div class='line' id='LC899'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Command </span><span class="si">%s</span><span class="s"> had error code </span><span class="si">%s</span><span class="s">&quot;</span></div><div class='line' id='LC900'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">%</span> <span class="p">(</span><span class="n">cmd_desc</span><span class="p">,</span> <span class="n">proc</span><span class="o">.</span><span class="n">returncode</span><span class="p">))</span></div><div class='line' id='LC901'><br/></div><div class='line' id='LC902'><span class="k">def</span> <span class="nf">filter_install_output</span><span class="p">(</span><span class="n">line</span><span class="p">):</span></div><div class='line' id='LC903'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;running&#39;</span><span class="p">):</span></div><div class='line' id='LC904'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Logger</span><span class="o">.</span><span class="n">INFO</span></div><div class='line' id='LC905'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Logger</span><span class="o">.</span><span class="n">DEBUG</span></div><div class='line' id='LC906'><br/></div><div class='line' id='LC907'><span class="k">def</span> <span class="nf">find_wheels</span><span class="p">(</span><span class="n">projects</span><span class="p">,</span> <span class="n">search_dirs</span><span class="p">):</span></div><div class='line' id='LC908'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Find wheels from which we can import PROJECTS.</span></div><div class='line' id='LC909'><br/></div><div class='line' id='LC910'><span class="sd">    Scan through SEARCH_DIRS for a wheel for each PROJECT in turn. Return</span></div><div class='line' id='LC911'><span class="sd">    a list of the first wheel found for each PROJECT</span></div><div class='line' id='LC912'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC913'><br/></div><div class='line' id='LC914'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">wheels</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC915'><br/></div><div class='line' id='LC916'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Look through SEARCH_DIRS for the first suitable wheel. Don&#39;t bother</span></div><div class='line' id='LC917'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># about version checking here, as this is simply to get something we can</span></div><div class='line' id='LC918'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># then use to install the correct version.</span></div><div class='line' id='LC919'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">project</span> <span class="ow">in</span> <span class="n">projects</span><span class="p">:</span></div><div class='line' id='LC920'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">dirname</span> <span class="ow">in</span> <span class="n">search_dirs</span><span class="p">:</span></div><div class='line' id='LC921'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># This relies on only having &quot;universal&quot; wheels available.</span></div><div class='line' id='LC922'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># The pattern could be tightened to require -py2.py3-none-any.whl.</span></div><div class='line' id='LC923'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span> <span class="o">=</span> <span class="n">glob</span><span class="o">.</span><span class="n">glob</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">dirname</span><span class="p">,</span> <span class="n">project</span> <span class="o">+</span> <span class="s">&#39;-*.whl&#39;</span><span class="p">))</span></div><div class='line' id='LC924'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">files</span><span class="p">:</span></div><div class='line' id='LC925'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">wheels</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">files</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span></div><div class='line' id='LC926'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC927'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC928'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># We&#39;re out of luck, so quit with a suitable error</span></div><div class='line' id='LC929'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span><span class="s">&#39;Cannot find a wheel for </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">project</span><span class="p">,))</span></div><div class='line' id='LC930'><br/></div><div class='line' id='LC931'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">wheels</span></div><div class='line' id='LC932'><br/></div><div class='line' id='LC933'><span class="k">def</span> <span class="nf">install_wheel</span><span class="p">(</span><span class="n">project_names</span><span class="p">,</span> <span class="n">py_executable</span><span class="p">,</span> <span class="n">search_dirs</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC934'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">search_dirs</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC935'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">search_dirs</span> <span class="o">=</span> <span class="n">file_search_dirs</span><span class="p">()</span></div><div class='line' id='LC936'><br/></div><div class='line' id='LC937'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">wheels</span> <span class="o">=</span> <span class="n">find_wheels</span><span class="p">([</span><span class="s">&#39;setuptools&#39;</span><span class="p">,</span> <span class="s">&#39;pip&#39;</span><span class="p">],</span> <span class="n">search_dirs</span><span class="p">)</span></div><div class='line' id='LC938'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pythonpath</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">pathsep</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">wheels</span><span class="p">)</span></div><div class='line' id='LC939'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">findlinks</span> <span class="o">=</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">search_dirs</span><span class="p">)</span></div><div class='line' id='LC940'><br/></div><div class='line' id='LC941'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cmd</span> <span class="o">=</span> <span class="p">[</span></div><div class='line' id='LC942'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_executable</span><span class="p">,</span> <span class="s">&#39;-c&#39;</span><span class="p">,</span></div><div class='line' id='LC943'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;import sys, pip; sys.exit(pip.main([&quot;install&quot;, &quot;--ignore-installed&quot;] + sys.argv[1:]))&#39;</span><span class="p">,</span></div><div class='line' id='LC944'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">]</span> <span class="o">+</span> <span class="n">project_names</span></div><div class='line' id='LC945'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">start_progress</span><span class="p">(</span><span class="s">&#39;Installing </span><span class="si">%s</span><span class="s">...&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">project_names</span><span class="p">)))</span></div><div class='line' id='LC946'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">indent</span> <span class="o">+=</span> <span class="mi">2</span></div><div class='line' id='LC947'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC948'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">call_subprocess</span><span class="p">(</span><span class="n">cmd</span><span class="p">,</span> <span class="n">show_stdout</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></div><div class='line' id='LC949'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">extra_env</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC950'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;PYTHONPATH&#39;</span><span class="p">:</span> <span class="n">pythonpath</span><span class="p">,</span></div><div class='line' id='LC951'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;PIP_FIND_LINKS&#39;</span><span class="p">:</span> <span class="n">findlinks</span><span class="p">,</span></div><div class='line' id='LC952'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;PIP_USE_WHEEL&#39;</span><span class="p">:</span> <span class="s">&#39;1&#39;</span><span class="p">,</span></div><div class='line' id='LC953'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;PIP_PRE&#39;</span><span class="p">:</span> <span class="s">&#39;1&#39;</span><span class="p">,</span></div><div class='line' id='LC954'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;PIP_NO_INDEX&#39;</span><span class="p">:</span> <span class="s">&#39;1&#39;</span></div><div class='line' id='LC955'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC956'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC957'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">finally</span><span class="p">:</span></div><div class='line' id='LC958'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">indent</span> <span class="o">-=</span> <span class="mi">2</span></div><div class='line' id='LC959'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">end_progress</span><span class="p">()</span></div><div class='line' id='LC960'><br/></div><div class='line' id='LC961'><span class="k">def</span> <span class="nf">create_environment</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="n">site_packages</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">clear</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></div><div class='line' id='LC962'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">unzip_setuptools</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></div><div class='line' id='LC963'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prompt</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">search_dirs</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">never_download</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></div><div class='line' id='LC964'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">no_setuptools</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">no_pip</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">symlink</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></div><div class='line' id='LC965'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC966'><span class="sd">    Creates a new environment in ``home_dir``.</span></div><div class='line' id='LC967'><br/></div><div class='line' id='LC968'><span class="sd">    If ``site_packages`` is true, then the global ``site-packages/``</span></div><div class='line' id='LC969'><span class="sd">    directory will be on the path.</span></div><div class='line' id='LC970'><br/></div><div class='line' id='LC971'><span class="sd">    If ``clear`` is true (default False) then the environment will</span></div><div class='line' id='LC972'><span class="sd">    first be cleared.</span></div><div class='line' id='LC973'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC974'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">home_dir</span><span class="p">,</span> <span class="n">lib_dir</span><span class="p">,</span> <span class="n">inc_dir</span><span class="p">,</span> <span class="n">bin_dir</span> <span class="o">=</span> <span class="n">path_locations</span><span class="p">(</span><span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC975'><br/></div><div class='line' id='LC976'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_executable</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">install_python</span><span class="p">(</span></div><div class='line' id='LC977'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">home_dir</span><span class="p">,</span> <span class="n">lib_dir</span><span class="p">,</span> <span class="n">inc_dir</span><span class="p">,</span> <span class="n">bin_dir</span><span class="p">,</span></div><div class='line' id='LC978'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">site_packages</span><span class="o">=</span><span class="n">site_packages</span><span class="p">,</span> <span class="n">clear</span><span class="o">=</span><span class="n">clear</span><span class="p">,</span> <span class="n">symlink</span><span class="o">=</span><span class="n">symlink</span><span class="p">))</span></div><div class='line' id='LC979'><br/></div><div class='line' id='LC980'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">install_distutils</span><span class="p">(</span><span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC981'><br/></div><div class='line' id='LC982'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">no_setuptools</span><span class="p">:</span></div><div class='line' id='LC983'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">to_install</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;setuptools&#39;</span><span class="p">]</span></div><div class='line' id='LC984'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">no_pip</span><span class="p">:</span></div><div class='line' id='LC985'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">to_install</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;pip&#39;</span><span class="p">)</span></div><div class='line' id='LC986'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">install_wheel</span><span class="p">(</span><span class="n">to_install</span><span class="p">,</span> <span class="n">py_executable</span><span class="p">,</span> <span class="n">search_dirs</span><span class="p">)</span></div><div class='line' id='LC987'><br/></div><div class='line' id='LC988'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">install_activate</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="n">bin_dir</span><span class="p">,</span> <span class="n">prompt</span><span class="p">)</span></div><div class='line' id='LC989'><br/></div><div class='line' id='LC990'><span class="k">def</span> <span class="nf">is_executable_file</span><span class="p">(</span><span class="n">fpath</span><span class="p">):</span></div><div class='line' id='LC991'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="n">fpath</span><span class="p">)</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">access</span><span class="p">(</span><span class="n">fpath</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">X_OK</span><span class="p">)</span></div><div class='line' id='LC992'><br/></div><div class='line' id='LC993'><span class="k">def</span> <span class="nf">path_locations</span><span class="p">(</span><span class="n">home_dir</span><span class="p">):</span></div><div class='line' id='LC994'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Return the path locations for the environment (where libraries are,</span></div><div class='line' id='LC995'><span class="sd">    where scripts go, etc)&quot;&quot;&quot;</span></div><div class='line' id='LC996'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># XXX: We&#39;d use distutils.sysconfig.get_python_inc/lib but its</span></div><div class='line' id='LC997'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># prefix arg is broken: http://bugs.python.org/issue3386</span></div><div class='line' id='LC998'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_win</span><span class="p">:</span></div><div class='line' id='LC999'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Windows has lots of problems with executables with spaces in</span></div><div class='line' id='LC1000'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># the name; this function will remove them (using the ~1</span></div><div class='line' id='LC1001'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># format):</span></div><div class='line' id='LC1002'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mkdir</span><span class="p">(</span><span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC1003'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39; &#39;</span> <span class="ow">in</span> <span class="n">home_dir</span><span class="p">:</span></div><div class='line' id='LC1004'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">ctypes</span></div><div class='line' id='LC1005'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">GetShortPathName</span> <span class="o">=</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">windll</span><span class="o">.</span><span class="n">kernel32</span><span class="o">.</span><span class="n">GetShortPathNameW</span></div><div class='line' id='LC1006'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">size</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">home_dir</span><span class="p">)</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span> <span class="mi">256</span><span class="p">)</span></div><div class='line' id='LC1007'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">buf</span> <span class="o">=</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">create_unicode_buffer</span><span class="p">(</span><span class="n">size</span><span class="p">)</span></div><div class='line' id='LC1008'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC1009'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">u</span> <span class="o">=</span> <span class="nb">unicode</span></div><div class='line' id='LC1010'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">NameError</span><span class="p">:</span></div><div class='line' id='LC1011'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">u</span> <span class="o">=</span> <span class="nb">str</span></div><div class='line' id='LC1012'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ret</span> <span class="o">=</span> <span class="n">GetShortPathName</span><span class="p">(</span><span class="n">u</span><span class="p">(</span><span class="n">home_dir</span><span class="p">),</span> <span class="n">buf</span><span class="p">,</span> <span class="n">size</span><span class="p">)</span></div><div class='line' id='LC1013'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">ret</span><span class="p">:</span></div><div class='line' id='LC1014'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="s">&#39;Error: the path &quot;</span><span class="si">%s</span><span class="s">&quot; has a space in it&#39;</span> <span class="o">%</span> <span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC1015'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="s">&#39;We could not determine the short pathname for it.&#39;</span><span class="p">)</span></div><div class='line' id='LC1016'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="s">&#39;Exiting.&#39;</span><span class="p">)</span></div><div class='line' id='LC1017'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span></div><div class='line' id='LC1018'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">home_dir</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">buf</span><span class="o">.</span><span class="n">value</span><span class="p">)</span></div><div class='line' id='LC1019'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lib_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;Lib&#39;</span><span class="p">)</span></div><div class='line' id='LC1020'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">inc_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;Include&#39;</span><span class="p">)</span></div><div class='line' id='LC1021'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bin_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;Scripts&#39;</span><span class="p">)</span></div><div class='line' id='LC1022'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_jython</span><span class="p">:</span></div><div class='line' id='LC1023'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lib_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;Lib&#39;</span><span class="p">)</span></div><div class='line' id='LC1024'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">inc_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;Include&#39;</span><span class="p">)</span></div><div class='line' id='LC1025'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bin_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;bin&#39;</span><span class="p">)</span></div><div class='line' id='LC1026'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">is_pypy</span><span class="p">:</span></div><div class='line' id='LC1027'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lib_dir</span> <span class="o">=</span> <span class="n">home_dir</span></div><div class='line' id='LC1028'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">inc_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;include&#39;</span><span class="p">)</span></div><div class='line' id='LC1029'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bin_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;bin&#39;</span><span class="p">)</span></div><div class='line' id='LC1030'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="ow">not</span> <span class="n">is_win</span><span class="p">:</span></div><div class='line' id='LC1031'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lib_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;lib&#39;</span><span class="p">,</span> <span class="n">py_version</span><span class="p">)</span></div><div class='line' id='LC1032'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">multiarch_exec</span> <span class="o">=</span> <span class="s">&#39;/usr/bin/multiarch-platform&#39;</span></div><div class='line' id='LC1033'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_executable_file</span><span class="p">(</span><span class="n">multiarch_exec</span><span class="p">):</span></div><div class='line' id='LC1034'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># In Mageia (2) and Mandriva distros the include dir must be like:</span></div><div class='line' id='LC1035'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># virtualenv/include/multiarch-x86_64-linux/python2.7</span></div><div class='line' id='LC1036'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># instead of being virtualenv/include/python2.7</span></div><div class='line' id='LC1037'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">(</span><span class="n">multiarch_exec</span><span class="p">,</span> <span class="n">stdout</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">,</span> <span class="n">stderr</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">)</span></div><div class='line' id='LC1038'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stdout</span><span class="p">,</span> <span class="n">stderr</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">communicate</span><span class="p">()</span></div><div class='line' id='LC1039'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># stdout.strip is needed to remove newline character</span></div><div class='line' id='LC1040'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">inc_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;include&#39;</span><span class="p">,</span> <span class="n">stdout</span><span class="o">.</span><span class="n">strip</span><span class="p">(),</span> <span class="n">py_version</span> <span class="o">+</span> <span class="n">abiflags</span><span class="p">)</span></div><div class='line' id='LC1041'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1042'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">inc_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;include&#39;</span><span class="p">,</span> <span class="n">py_version</span> <span class="o">+</span> <span class="n">abiflags</span><span class="p">)</span></div><div class='line' id='LC1043'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bin_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;bin&#39;</span><span class="p">)</span></div><div class='line' id='LC1044'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">home_dir</span><span class="p">,</span> <span class="n">lib_dir</span><span class="p">,</span> <span class="n">inc_dir</span><span class="p">,</span> <span class="n">bin_dir</span></div><div class='line' id='LC1045'><br/></div><div class='line' id='LC1046'><br/></div><div class='line' id='LC1047'><span class="k">def</span> <span class="nf">change_prefix</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">dst_prefix</span><span class="p">):</span></div><div class='line' id='LC1048'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefixes</span> <span class="o">=</span> <span class="p">[</span><span class="n">sys</span><span class="o">.</span><span class="n">prefix</span><span class="p">]</span></div><div class='line' id='LC1049'><br/></div><div class='line' id='LC1050'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_darwin</span><span class="p">:</span></div><div class='line' id='LC1051'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefixes</span><span class="o">.</span><span class="n">extend</span><span class="p">((</span></div><div class='line' id='LC1052'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s">&quot;/Library/Python&quot;</span><span class="p">,</span> <span class="n">sys</span><span class="o">.</span><span class="n">version</span><span class="p">[:</span><span class="mi">3</span><span class="p">],</span> <span class="s">&quot;site-packages&quot;</span><span class="p">),</span></div><div class='line' id='LC1053'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">prefix</span><span class="p">,</span> <span class="s">&quot;Extras&quot;</span><span class="p">,</span> <span class="s">&quot;lib&quot;</span><span class="p">,</span> <span class="s">&quot;python&quot;</span><span class="p">),</span></div><div class='line' id='LC1054'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s">&quot;~&quot;</span><span class="p">,</span> <span class="s">&quot;Library&quot;</span><span class="p">,</span> <span class="s">&quot;Python&quot;</span><span class="p">,</span> <span class="n">sys</span><span class="o">.</span><span class="n">version</span><span class="p">[:</span><span class="mi">3</span><span class="p">],</span> <span class="s">&quot;site-packages&quot;</span><span class="p">),</span></div><div class='line' id='LC1055'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Python 2.6 no-frameworks</span></div><div class='line' id='LC1056'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s">&quot;~&quot;</span><span class="p">,</span> <span class="s">&quot;.local&quot;</span><span class="p">,</span> <span class="s">&quot;lib&quot;</span><span class="p">,</span><span class="s">&quot;python&quot;</span><span class="p">,</span> <span class="n">sys</span><span class="o">.</span><span class="n">version</span><span class="p">[:</span><span class="mi">3</span><span class="p">],</span> <span class="s">&quot;site-packages&quot;</span><span class="p">),</span></div><div class='line' id='LC1057'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># System Python 2.7 on OSX Mountain Lion</span></div><div class='line' id='LC1058'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s">&quot;~&quot;</span><span class="p">,</span> <span class="s">&quot;Library&quot;</span><span class="p">,</span> <span class="s">&quot;Python&quot;</span><span class="p">,</span> <span class="n">sys</span><span class="o">.</span><span class="n">version</span><span class="p">[:</span><span class="mi">3</span><span class="p">],</span> <span class="s">&quot;lib&quot;</span><span class="p">,</span> <span class="s">&quot;python&quot;</span><span class="p">,</span> <span class="s">&quot;site-packages&quot;</span><span class="p">)))</span></div><div class='line' id='LC1059'><br/></div><div class='line' id='LC1060'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">sys</span><span class="p">,</span> <span class="s">&#39;real_prefix&#39;</span><span class="p">):</span></div><div class='line' id='LC1061'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefixes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">real_prefix</span><span class="p">)</span></div><div class='line' id='LC1062'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">sys</span><span class="p">,</span> <span class="s">&#39;base_prefix&#39;</span><span class="p">):</span></div><div class='line' id='LC1063'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefixes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">base_prefix</span><span class="p">)</span></div><div class='line' id='LC1064'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefixes</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">expanduser</span><span class="p">,</span> <span class="n">prefixes</span><span class="p">))</span></div><div class='line' id='LC1065'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefixes</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">,</span> <span class="n">prefixes</span><span class="p">))</span></div><div class='line' id='LC1066'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Check longer prefixes first so we don&#39;t split in the middle of a filename</span></div><div class='line' id='LC1067'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefixes</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">prefixes</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="nb">len</span><span class="p">,</span> <span class="n">reverse</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC1068'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1069'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">src_prefix</span> <span class="ow">in</span> <span class="n">prefixes</span><span class="p">:</span></div><div class='line' id='LC1070'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">filename</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">src_prefix</span><span class="p">):</span></div><div class='line' id='LC1071'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">_</span><span class="p">,</span> <span class="n">relpath</span> <span class="o">=</span> <span class="n">filename</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">src_prefix</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC1072'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">src_prefix</span> <span class="o">!=</span> <span class="n">os</span><span class="o">.</span><span class="n">sep</span><span class="p">:</span> <span class="c"># sys.prefix == &quot;/&quot;</span></div><div class='line' id='LC1073'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">relpath</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="n">os</span><span class="o">.</span><span class="n">sep</span></div><div class='line' id='LC1074'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">relpath</span> <span class="o">=</span> <span class="n">relpath</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span></div><div class='line' id='LC1075'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">join</span><span class="p">(</span><span class="n">dst_prefix</span><span class="p">,</span> <span class="n">relpath</span><span class="p">)</span></div><div class='line' id='LC1076'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="bp">False</span><span class="p">,</span> <span class="s">&quot;Filename </span><span class="si">%s</span><span class="s"> does not start with any of these prefixes: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> \</div><div class='line' id='LC1077'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">prefixes</span><span class="p">)</span></div><div class='line' id='LC1078'><br/></div><div class='line' id='LC1079'><span class="k">def</span> <span class="nf">copy_required_modules</span><span class="p">(</span><span class="n">dst_prefix</span><span class="p">,</span> <span class="n">symlink</span><span class="p">):</span></div><div class='line' id='LC1080'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">imp</span></div><div class='line' id='LC1081'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># If we are running under -p, we need to remove the current</span></div><div class='line' id='LC1082'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># directory from sys.path temporarily here, so that we</span></div><div class='line' id='LC1083'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># definitely get the modules from the site directory of</span></div><div class='line' id='LC1084'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># the interpreter we are running under, not the one</span></div><div class='line' id='LC1085'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># virtualenv.py is installed under (which might lead to py2/py3</span></div><div class='line' id='LC1086'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># incompatibility issues)</span></div><div class='line' id='LC1087'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">_prev_sys_path</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">path</span></div><div class='line' id='LC1088'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;VIRTUALENV_INTERPRETER_RUNNING&#39;</span><span class="p">):</span></div><div class='line' id='LC1089'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">path</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">path</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span></div><div class='line' id='LC1090'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC1091'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">modname</span> <span class="ow">in</span> <span class="n">REQUIRED_MODULES</span><span class="p">:</span></div><div class='line' id='LC1092'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">modname</span> <span class="ow">in</span> <span class="n">sys</span><span class="o">.</span><span class="n">builtin_module_names</span><span class="p">:</span></div><div class='line' id='LC1093'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&quot;Ignoring built-in bootstrap module: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">modname</span><span class="p">)</span></div><div class='line' id='LC1094'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC1095'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC1096'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="p">,</span> <span class="n">filename</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">imp</span><span class="o">.</span><span class="n">find_module</span><span class="p">(</span><span class="n">modname</span><span class="p">)</span></div><div class='line' id='LC1097'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div><div class='line' id='LC1098'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&quot;Cannot import bootstrap module: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">modname</span><span class="p">)</span></div><div class='line' id='LC1099'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">f</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC1101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC1102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># special-case custom readline.so on OS X, but not for pypy:</span></div><div class='line' id='LC1103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">modname</span> <span class="o">==</span> <span class="s">&#39;readline&#39;</span> <span class="ow">and</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s">&#39;darwin&#39;</span> <span class="ow">and</span> <span class="ow">not</span> <span class="p">(</span></div><div class='line' id='LC1104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">is_pypy</span> <span class="ow">or</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="n">join</span><span class="p">(</span><span class="s">&#39;lib-dynload&#39;</span><span class="p">,</span> <span class="s">&#39;readline.so&#39;</span><span class="p">))):</span></div><div class='line' id='LC1105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dst_filename</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">dst_prefix</span><span class="p">,</span> <span class="s">&#39;lib&#39;</span><span class="p">,</span> <span class="s">&#39;python</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">sys</span><span class="o">.</span><span class="n">version</span><span class="p">[:</span><span class="mi">3</span><span class="p">],</span> <span class="s">&#39;readline.so&#39;</span><span class="p">)</span></div><div class='line' id='LC1106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">modname</span> <span class="o">==</span> <span class="s">&#39;readline&#39;</span> <span class="ow">and</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s">&#39;win32&#39;</span><span class="p">:</span></div><div class='line' id='LC1107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># special-case for Windows, where readline is not a</span></div><div class='line' id='LC1108'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># standard module, though it may have been installed in</span></div><div class='line' id='LC1109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># site-packages by a third-party package</span></div><div class='line' id='LC1110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dst_filename</span> <span class="o">=</span> <span class="n">change_prefix</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">dst_prefix</span><span class="p">)</span></div><div class='line' id='LC1113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">dst_filename</span><span class="p">,</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;.pyc&#39;</span><span class="p">):</span></div><div class='line' id='LC1115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pyfile</span> <span class="o">=</span> <span class="n">filename</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC1116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">pyfile</span><span class="p">):</span></div><div class='line' id='LC1117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span><span class="n">pyfile</span><span class="p">,</span> <span class="n">dst_filename</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1118'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">finally</span><span class="p">:</span></div><div class='line' id='LC1119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">path</span> <span class="o">=</span> <span class="n">_prev_sys_path</span></div><div class='line' id='LC1120'><br/></div><div class='line' id='LC1121'><br/></div><div class='line' id='LC1122'><span class="k">def</span> <span class="nf">subst_path</span><span class="p">(</span><span class="n">prefix_path</span><span class="p">,</span> <span class="n">prefix</span><span class="p">,</span> <span class="n">home_dir</span><span class="p">):</span></div><div class='line' id='LC1123'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefix_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normpath</span><span class="p">(</span><span class="n">prefix_path</span><span class="p">)</span></div><div class='line' id='LC1124'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefix</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normpath</span><span class="p">(</span><span class="n">prefix</span><span class="p">)</span></div><div class='line' id='LC1125'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">home_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normpath</span><span class="p">(</span><span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC1126'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">prefix_path</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">prefix</span><span class="p">):</span></div><div class='line' id='LC1127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&#39;Path not in prefix </span><span class="si">%r</span><span class="s"> </span><span class="si">%r</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">prefix_path</span><span class="p">,</span> <span class="n">prefix</span><span class="p">)</span></div><div class='line' id='LC1128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC1129'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">prefix_path</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">home_dir</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC1130'><br/></div><div class='line' id='LC1131'><br/></div><div class='line' id='LC1132'><span class="k">def</span> <span class="nf">install_python</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="n">lib_dir</span><span class="p">,</span> <span class="n">inc_dir</span><span class="p">,</span> <span class="n">bin_dir</span><span class="p">,</span> <span class="n">site_packages</span><span class="p">,</span> <span class="n">clear</span><span class="p">,</span> <span class="n">symlink</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></div><div class='line' id='LC1133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Install just the base environment, no distutils patches etc&quot;&quot;&quot;</span></div><div class='line' id='LC1134'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">bin_dir</span><span class="p">):</span></div><div class='line' id='LC1135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span><span class="p">(</span><span class="s">&#39;Please use the *system* python to run this script&#39;</span><span class="p">)</span></div><div class='line' id='LC1136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC1137'><br/></div><div class='line' id='LC1138'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">clear</span><span class="p">:</span></div><div class='line' id='LC1139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rmtree</span><span class="p">(</span><span class="n">lib_dir</span><span class="p">)</span></div><div class='line' id='LC1140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">## FIXME: why not delete it?</span></div><div class='line' id='LC1141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">## Maybe it should delete everything with #!/path/to/venv/python in it</span></div><div class='line' id='LC1142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Not deleting </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">bin_dir</span><span class="p">)</span></div><div class='line' id='LC1143'><br/></div><div class='line' id='LC1144'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">sys</span><span class="p">,</span> <span class="s">&#39;real_prefix&#39;</span><span class="p">):</span></div><div class='line' id='LC1145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Using real prefix </span><span class="si">%r</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">sys</span><span class="o">.</span><span class="n">real_prefix</span><span class="p">)</span></div><div class='line' id='LC1146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefix</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">real_prefix</span></div><div class='line' id='LC1147'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">sys</span><span class="p">,</span> <span class="s">&#39;base_prefix&#39;</span><span class="p">):</span></div><div class='line' id='LC1148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Using base prefix </span><span class="si">%r</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">sys</span><span class="o">.</span><span class="n">base_prefix</span><span class="p">)</span></div><div class='line' id='LC1149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefix</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">base_prefix</span></div><div class='line' id='LC1150'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1151'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefix</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">prefix</span></div><div class='line' id='LC1152'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mkdir</span><span class="p">(</span><span class="n">lib_dir</span><span class="p">)</span></div><div class='line' id='LC1153'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fix_lib64</span><span class="p">(</span><span class="n">lib_dir</span><span class="p">,</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1154'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stdlib_dirs</span> <span class="o">=</span> <span class="p">[</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">__file__</span><span class="p">)]</span></div><div class='line' id='LC1155'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_win</span><span class="p">:</span></div><div class='line' id='LC1156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stdlib_dirs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">stdlib_dirs</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span> <span class="s">&#39;DLLs&#39;</span><span class="p">))</span></div><div class='line' id='LC1157'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">is_darwin</span><span class="p">:</span></div><div class='line' id='LC1158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stdlib_dirs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">join</span><span class="p">(</span><span class="n">stdlib_dirs</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="s">&#39;site-packages&#39;</span><span class="p">))</span></div><div class='line' id='LC1159'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">os</span><span class="p">,</span> <span class="s">&#39;symlink&#39;</span><span class="p">):</span></div><div class='line' id='LC1160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Symlinking Python bootstrap modules&#39;</span><span class="p">)</span></div><div class='line' id='LC1161'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1162'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Copying Python bootstrap modules&#39;</span><span class="p">)</span></div><div class='line' id='LC1163'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">indent</span> <span class="o">+=</span> <span class="mi">2</span></div><div class='line' id='LC1164'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC1165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># copy required files...</span></div><div class='line' id='LC1166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">stdlib_dir</span> <span class="ow">in</span> <span class="n">stdlib_dirs</span><span class="p">:</span></div><div class='line' id='LC1167'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="n">stdlib_dir</span><span class="p">):</span></div><div class='line' id='LC1168'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC1169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">fn</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">stdlib_dir</span><span class="p">):</span></div><div class='line' id='LC1170'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bn</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="n">fn</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC1171'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">fn</span> <span class="o">!=</span> <span class="s">&#39;site-packages&#39;</span> <span class="ow">and</span> <span class="n">bn</span> <span class="ow">in</span> <span class="n">REQUIRED_FILES</span><span class="p">:</span></div><div class='line' id='LC1172'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span><span class="n">join</span><span class="p">(</span><span class="n">stdlib_dir</span><span class="p">,</span> <span class="n">fn</span><span class="p">),</span> <span class="n">join</span><span class="p">(</span><span class="n">lib_dir</span><span class="p">,</span> <span class="n">fn</span><span class="p">),</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1173'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># ...and modules</span></div><div class='line' id='LC1174'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copy_required_modules</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1175'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">finally</span><span class="p">:</span></div><div class='line' id='LC1176'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">indent</span> <span class="o">-=</span> <span class="mi">2</span></div><div class='line' id='LC1177'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mkdir</span><span class="p">(</span><span class="n">join</span><span class="p">(</span><span class="n">lib_dir</span><span class="p">,</span> <span class="s">&#39;site-packages&#39;</span><span class="p">))</span></div><div class='line' id='LC1178'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">site</span></div><div class='line' id='LC1179'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">site_filename</span> <span class="o">=</span> <span class="n">site</span><span class="o">.</span><span class="n">__file__</span></div><div class='line' id='LC1180'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">site_filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;.pyc&#39;</span><span class="p">):</span></div><div class='line' id='LC1181'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">site_filename</span> <span class="o">=</span> <span class="n">site_filename</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC1182'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">site_filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;$py.class&#39;</span><span class="p">):</span></div><div class='line' id='LC1183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">site_filename</span> <span class="o">=</span> <span class="n">site_filename</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;$py.class&#39;</span><span class="p">,</span> <span class="s">&#39;.py&#39;</span><span class="p">)</span></div><div class='line' id='LC1184'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">site_filename_dst</span> <span class="o">=</span> <span class="n">change_prefix</span><span class="p">(</span><span class="n">site_filename</span><span class="p">,</span> <span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC1185'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">site_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">site_filename_dst</span><span class="p">)</span></div><div class='line' id='LC1186'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writefile</span><span class="p">(</span><span class="n">site_filename_dst</span><span class="p">,</span> <span class="n">SITE_PY</span><span class="p">)</span></div><div class='line' id='LC1187'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writefile</span><span class="p">(</span><span class="n">join</span><span class="p">(</span><span class="n">site_dir</span><span class="p">,</span> <span class="s">&#39;orig-prefix.txt&#39;</span><span class="p">),</span> <span class="n">prefix</span><span class="p">)</span></div><div class='line' id='LC1188'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">site_packages_filename</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">site_dir</span><span class="p">,</span> <span class="s">&#39;no-global-site-packages.txt&#39;</span><span class="p">)</span></div><div class='line' id='LC1189'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">site_packages</span><span class="p">:</span></div><div class='line' id='LC1190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writefile</span><span class="p">(</span><span class="n">site_packages_filename</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC1191'><br/></div><div class='line' id='LC1192'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_pypy</span> <span class="ow">or</span> <span class="n">is_win</span><span class="p">:</span></div><div class='line' id='LC1193'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stdinc_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="s">&#39;include&#39;</span><span class="p">)</span></div><div class='line' id='LC1194'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1195'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stdinc_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="s">&#39;include&#39;</span><span class="p">,</span> <span class="n">py_version</span> <span class="o">+</span> <span class="n">abiflags</span><span class="p">)</span></div><div class='line' id='LC1196'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">stdinc_dir</span><span class="p">):</span></div><div class='line' id='LC1197'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span><span class="n">stdinc_dir</span><span class="p">,</span> <span class="n">inc_dir</span><span class="p">,</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1198'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1199'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;No include dir </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">stdinc_dir</span><span class="p">)</span></div><div class='line' id='LC1200'><br/></div><div class='line' id='LC1201'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platinc_dir</span> <span class="o">=</span> <span class="n">distutils</span><span class="o">.</span><span class="n">sysconfig</span><span class="o">.</span><span class="n">get_python_inc</span><span class="p">(</span><span class="n">plat_specific</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC1202'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">platinc_dir</span> <span class="o">!=</span> <span class="n">stdinc_dir</span><span class="p">:</span></div><div class='line' id='LC1203'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platinc_dest</span> <span class="o">=</span> <span class="n">distutils</span><span class="o">.</span><span class="n">sysconfig</span><span class="o">.</span><span class="n">get_python_inc</span><span class="p">(</span></div><div class='line' id='LC1204'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">plat_specific</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">prefix</span><span class="o">=</span><span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC1205'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">platinc_dir</span> <span class="o">==</span> <span class="n">platinc_dest</span><span class="p">:</span></div><div class='line' id='LC1206'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Do platinc_dest manually due to a CPython bug;</span></div><div class='line' id='LC1207'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># not http://bugs.python.org/issue3386 but a close cousin</span></div><div class='line' id='LC1208'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platinc_dest</span> <span class="o">=</span> <span class="n">subst_path</span><span class="p">(</span><span class="n">platinc_dir</span><span class="p">,</span> <span class="n">prefix</span><span class="p">,</span> <span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC1209'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">platinc_dest</span><span class="p">:</span></div><div class='line' id='LC1210'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># PyPy&#39;s stdinc_dir and prefix are relative to the original binary</span></div><div class='line' id='LC1211'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># (traversing virtualenvs), whereas the platinc_dir is relative to</span></div><div class='line' id='LC1212'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># the inner virtualenv and ignores the prefix argument.</span></div><div class='line' id='LC1213'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># This seems more evolved than designed.</span></div><div class='line' id='LC1214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span><span class="n">platinc_dir</span><span class="p">,</span> <span class="n">platinc_dest</span><span class="p">,</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1215'><br/></div><div class='line' id='LC1216'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># pypy never uses exec_prefix, just ignore it</span></div><div class='line' id='LC1217'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">exec_prefix</span> <span class="o">!=</span> <span class="n">prefix</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">is_pypy</span><span class="p">:</span></div><div class='line' id='LC1218'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_win</span><span class="p">:</span></div><div class='line' id='LC1219'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">exec_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">exec_prefix</span><span class="p">,</span> <span class="s">&#39;lib&#39;</span><span class="p">)</span></div><div class='line' id='LC1220'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">is_jython</span><span class="p">:</span></div><div class='line' id='LC1221'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">exec_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">exec_prefix</span><span class="p">,</span> <span class="s">&#39;Lib&#39;</span><span class="p">)</span></div><div class='line' id='LC1222'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1223'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">exec_dir</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">exec_prefix</span><span class="p">,</span> <span class="s">&#39;lib&#39;</span><span class="p">,</span> <span class="n">py_version</span><span class="p">)</span></div><div class='line' id='LC1224'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">fn</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">exec_dir</span><span class="p">):</span></div><div class='line' id='LC1225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span><span class="n">join</span><span class="p">(</span><span class="n">exec_dir</span><span class="p">,</span> <span class="n">fn</span><span class="p">),</span> <span class="n">join</span><span class="p">(</span><span class="n">lib_dir</span><span class="p">,</span> <span class="n">fn</span><span class="p">),</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1226'><br/></div><div class='line' id='LC1227'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_jython</span><span class="p">:</span></div><div class='line' id='LC1228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Jython has either jython-dev.jar and javalib/ dir, or just</span></div><div class='line' id='LC1229'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># jython.jar</span></div><div class='line' id='LC1230'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="s">&#39;jython-dev.jar&#39;</span><span class="p">,</span> <span class="s">&#39;javalib&#39;</span><span class="p">,</span> <span class="s">&#39;jython.jar&#39;</span><span class="p">:</span></div><div class='line' id='LC1231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span></div><div class='line' id='LC1232'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">src</span><span class="p">):</span></div><div class='line' id='LC1233'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span><span class="n">src</span><span class="p">,</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="n">name</span><span class="p">),</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1234'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># XXX: registry should always exist after Jython 2.5rc1</span></div><div class='line' id='LC1235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="s">&#39;registry&#39;</span><span class="p">)</span></div><div class='line' id='LC1236'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">src</span><span class="p">):</span></div><div class='line' id='LC1237'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span><span class="n">src</span><span class="p">,</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;registry&#39;</span><span class="p">),</span> <span class="n">symlink</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC1238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span><span class="n">join</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="s">&#39;cachedir&#39;</span><span class="p">),</span> <span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;cachedir&#39;</span><span class="p">),</span></div><div class='line' id='LC1239'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">symlink</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC1240'><br/></div><div class='line' id='LC1241'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mkdir</span><span class="p">(</span><span class="n">bin_dir</span><span class="p">)</span></div><div class='line' id='LC1242'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_executable</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">bin_dir</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">))</span></div><div class='line' id='LC1243'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;Python.framework&#39;</span> <span class="ow">in</span> <span class="n">prefix</span><span class="p">:</span></div><div class='line' id='LC1244'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># OS X framework builds cause validation to break</span></div><div class='line' id='LC1245'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># https://github.com/pypa/virtualenv/issues/322</span></div><div class='line' id='LC1246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;__PYVENV_LAUNCHER__&#39;</span><span class="p">):</span></div><div class='line' id='LC1247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">del</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s">&quot;__PYVENV_LAUNCHER__&quot;</span><span class="p">]</span></div><div class='line' id='LC1248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">re</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="s">r&#39;/Python(?:-32|-64)*$&#39;</span><span class="p">,</span> <span class="n">py_executable</span><span class="p">):</span></div><div class='line' id='LC1249'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># The name of the python executable is not quite what</span></div><div class='line' id='LC1250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># we want, rename it.</span></div><div class='line' id='LC1251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_executable</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span></div><div class='line' id='LC1252'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">py_executable</span><span class="p">),</span> <span class="s">&#39;python&#39;</span><span class="p">)</span></div><div class='line' id='LC1253'><br/></div><div class='line' id='LC1254'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;New </span><span class="si">%s</span><span class="s"> executable in </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">expected_exe</span><span class="p">,</span> <span class="n">py_executable</span><span class="p">)</span></div><div class='line' id='LC1255'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pcbuild_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">)</span></div><div class='line' id='LC1256'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pyd_pth</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lib_dir</span><span class="p">,</span> <span class="s">&#39;site-packages&#39;</span><span class="p">,</span> <span class="s">&#39;virtualenv_builddir_pyd.pth&#39;</span><span class="p">)</span></div><div class='line' id='LC1257'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_win</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">pcbuild_dir</span><span class="p">,</span> <span class="s">&#39;build.bat&#39;</span><span class="p">)):</span></div><div class='line' id='LC1258'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Detected python running from build directory </span><span class="si">%s</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">pcbuild_dir</span><span class="p">)</span></div><div class='line' id='LC1259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Writing .pth file linking to build directory for *.pyd files&#39;</span><span class="p">)</span></div><div class='line' id='LC1260'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writefile</span><span class="p">(</span><span class="n">pyd_pth</span><span class="p">,</span> <span class="n">pcbuild_dir</span><span class="p">)</span></div><div class='line' id='LC1261'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1262'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pcbuild_dir</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC1263'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">pyd_pth</span><span class="p">):</span></div><div class='line' id='LC1264'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Deleting </span><span class="si">%s</span><span class="s"> (not Windows env or not build directory python)&#39;</span> <span class="o">%</span> <span class="n">pyd_pth</span><span class="p">)</span></div><div class='line' id='LC1265'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">unlink</span><span class="p">(</span><span class="n">pyd_pth</span><span class="p">)</span></div><div class='line' id='LC1266'><br/></div><div class='line' id='LC1267'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">executable</span> <span class="o">!=</span> <span class="n">py_executable</span><span class="p">:</span></div><div class='line' id='LC1268'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">## FIXME: could I just hard link?</span></div><div class='line' id='LC1269'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">executable</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">executable</span></div><div class='line' id='LC1270'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">copyfile</span><span class="p">(</span><span class="n">executable</span><span class="p">,</span> <span class="n">py_executable</span><span class="p">)</span></div><div class='line' id='LC1271'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">make_exe</span><span class="p">(</span><span class="n">py_executable</span><span class="p">)</span></div><div class='line' id='LC1272'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_win</span> <span class="ow">or</span> <span class="n">is_cygwin</span><span class="p">:</span></div><div class='line' id='LC1273'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pythonw</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">),</span> <span class="s">&#39;pythonw.exe&#39;</span><span class="p">)</span></div><div class='line' id='LC1274'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">pythonw</span><span class="p">):</span></div><div class='line' id='LC1275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Also created pythonw.exe&#39;</span><span class="p">)</span></div><div class='line' id='LC1276'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">copyfile</span><span class="p">(</span><span class="n">pythonw</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">py_executable</span><span class="p">),</span> <span class="s">&#39;pythonw.exe&#39;</span><span class="p">))</span></div><div class='line' id='LC1277'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">python_d</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">),</span> <span class="s">&#39;python_d.exe&#39;</span><span class="p">)</span></div><div class='line' id='LC1278'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">python_d_dest</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">py_executable</span><span class="p">),</span> <span class="s">&#39;python_d.exe&#39;</span><span class="p">)</span></div><div class='line' id='LC1279'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">python_d</span><span class="p">):</span></div><div class='line' id='LC1280'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Also created python_d.exe&#39;</span><span class="p">)</span></div><div class='line' id='LC1281'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">copyfile</span><span class="p">(</span><span class="n">python_d</span><span class="p">,</span> <span class="n">python_d_dest</span><span class="p">)</span></div><div class='line' id='LC1282'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">python_d_dest</span><span class="p">):</span></div><div class='line' id='LC1283'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Removed python_d.exe as it is no longer at the source&#39;</span><span class="p">)</span></div><div class='line' id='LC1284'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">unlink</span><span class="p">(</span><span class="n">python_d_dest</span><span class="p">)</span></div><div class='line' id='LC1285'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># we need to copy the DLL to enforce that windows will load the correct one.</span></div><div class='line' id='LC1286'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># may not exist if we are cygwin.</span></div><div class='line' id='LC1287'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_executable_dll</span> <span class="o">=</span> <span class="s">&#39;python</span><span class="si">%s%s</span><span class="s">.dll&#39;</span> <span class="o">%</span> <span class="p">(</span></div><div class='line' id='LC1288'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC1289'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_executable_dll_d</span> <span class="o">=</span> <span class="s">&#39;python</span><span class="si">%s%s</span><span class="s">_d.dll&#39;</span> <span class="o">%</span> <span class="p">(</span></div><div class='line' id='LC1290'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC1291'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pythondll</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">),</span> <span class="n">py_executable_dll</span><span class="p">)</span></div><div class='line' id='LC1292'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pythondll_d</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">),</span> <span class="n">py_executable_dll_d</span><span class="p">)</span></div><div class='line' id='LC1293'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pythondll_d_dest</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">py_executable</span><span class="p">),</span> <span class="n">py_executable_dll_d</span><span class="p">)</span></div><div class='line' id='LC1294'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">pythondll</span><span class="p">):</span></div><div class='line' id='LC1295'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Also created </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">py_executable_dll</span><span class="p">)</span></div><div class='line' id='LC1296'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">copyfile</span><span class="p">(</span><span class="n">pythondll</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">py_executable</span><span class="p">),</span> <span class="n">py_executable_dll</span><span class="p">))</span></div><div class='line' id='LC1297'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">pythondll_d</span><span class="p">):</span></div><div class='line' id='LC1298'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Also created </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">py_executable_dll_d</span><span class="p">)</span></div><div class='line' id='LC1299'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">copyfile</span><span class="p">(</span><span class="n">pythondll_d</span><span class="p">,</span> <span class="n">pythondll_d_dest</span><span class="p">)</span></div><div class='line' id='LC1300'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">pythondll_d_dest</span><span class="p">):</span></div><div class='line' id='LC1301'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Removed </span><span class="si">%s</span><span class="s"> as the source does not exist&#39;</span> <span class="o">%</span> <span class="n">pythondll_d_dest</span><span class="p">)</span></div><div class='line' id='LC1302'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">unlink</span><span class="p">(</span><span class="n">pythondll_d_dest</span><span class="p">)</span></div><div class='line' id='LC1303'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_pypy</span><span class="p">:</span></div><div class='line' id='LC1304'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># make a symlink python --&gt; pypy-c</span></div><div class='line' id='LC1305'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">python_executable</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">py_executable</span><span class="p">),</span> <span class="s">&#39;python&#39;</span><span class="p">)</span></div><div class='line' id='LC1306'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&#39;win32&#39;</span><span class="p">,</span> <span class="s">&#39;cygwin&#39;</span><span class="p">):</span></div><div class='line' id='LC1307'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">python_executable</span> <span class="o">+=</span> <span class="s">&#39;.exe&#39;</span></div><div class='line' id='LC1308'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Also created executable </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">python_executable</span><span class="p">)</span></div><div class='line' id='LC1309'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span><span class="n">py_executable</span><span class="p">,</span> <span class="n">python_executable</span><span class="p">,</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1310'><br/></div><div class='line' id='LC1311'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_win</span><span class="p">:</span></div><div class='line' id='LC1312'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="s">&#39;libexpat.dll&#39;</span><span class="p">,</span> <span class="s">&#39;libpypy.dll&#39;</span><span class="p">,</span> <span class="s">&#39;libpypy-c.dll&#39;</span><span class="p">,</span> <span class="s">&#39;libeay32.dll&#39;</span><span class="p">,</span> <span class="s">&#39;ssleay32.dll&#39;</span><span class="p">,</span> <span class="s">&#39;sqlite.dll&#39;</span><span class="p">:</span></div><div class='line' id='LC1313'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span></div><div class='line' id='LC1314'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">src</span><span class="p">):</span></div><div class='line' id='LC1315'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span><span class="n">src</span><span class="p">,</span> <span class="n">join</span><span class="p">(</span><span class="n">bin_dir</span><span class="p">,</span> <span class="n">name</span><span class="p">),</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1316'><br/></div><div class='line' id='LC1317'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">py_executable</span><span class="p">))[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="n">expected_exe</span><span class="p">:</span></div><div class='line' id='LC1318'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">secondary_exe</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">py_executable</span><span class="p">),</span></div><div class='line' id='LC1319'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">expected_exe</span><span class="p">)</span></div><div class='line' id='LC1320'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_executable_ext</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="n">py_executable</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC1321'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">py_executable_ext</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="o">==</span> <span class="s">&#39;.exe&#39;</span><span class="p">:</span></div><div class='line' id='LC1322'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># python2.4 gives an extension of &#39;.4&#39; :P</span></div><div class='line' id='LC1323'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">secondary_exe</span> <span class="o">+=</span> <span class="n">py_executable_ext</span></div><div class='line' id='LC1324'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">secondary_exe</span><span class="p">):</span></div><div class='line' id='LC1325'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&#39;Not overwriting existing </span><span class="si">%s</span><span class="s"> script </span><span class="si">%s</span><span class="s"> (you must use </span><span class="si">%s</span><span class="s">)&#39;</span></div><div class='line' id='LC1326'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">%</span> <span class="p">(</span><span class="n">expected_exe</span><span class="p">,</span> <span class="n">secondary_exe</span><span class="p">,</span> <span class="n">py_executable</span><span class="p">))</span></div><div class='line' id='LC1327'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1328'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Also creating executable in </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">secondary_exe</span><span class="p">)</span></div><div class='line' id='LC1329'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">copyfile</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">,</span> <span class="n">secondary_exe</span><span class="p">)</span></div><div class='line' id='LC1330'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">make_exe</span><span class="p">(</span><span class="n">secondary_exe</span><span class="p">)</span></div><div class='line' id='LC1331'><br/></div><div class='line' id='LC1332'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;.framework&#39;</span> <span class="ow">in</span> <span class="n">prefix</span><span class="p">:</span></div><div class='line' id='LC1333'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;Python.framework&#39;</span> <span class="ow">in</span> <span class="n">prefix</span><span class="p">:</span></div><div class='line' id='LC1334'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;MacOSX Python framework detected&#39;</span><span class="p">)</span></div><div class='line' id='LC1335'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Make sure we use the the embedded interpreter inside</span></div><div class='line' id='LC1336'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># the framework, even if sys.executable points to</span></div><div class='line' id='LC1337'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># the stub executable in ${sys.prefix}/bin</span></div><div class='line' id='LC1338'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># See http://groups.google.com/group/python-virtualenv/</span></div><div class='line' id='LC1339'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#                              browse_thread/thread/17cab2f85da75951</span></div><div class='line' id='LC1340'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">original_python</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span></div><div class='line' id='LC1341'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefix</span><span class="p">,</span> <span class="s">&#39;Resources/Python.app/Contents/MacOS/Python&#39;</span><span class="p">)</span></div><div class='line' id='LC1342'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;EPD&#39;</span> <span class="ow">in</span> <span class="n">prefix</span><span class="p">:</span></div><div class='line' id='LC1343'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;EPD framework detected&#39;</span><span class="p">)</span></div><div class='line' id='LC1344'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">original_python</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="s">&#39;bin/python&#39;</span><span class="p">)</span></div><div class='line' id='LC1345'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">original_python</span><span class="p">,</span> <span class="n">py_executable</span><span class="p">)</span></div><div class='line' id='LC1346'><br/></div><div class='line' id='LC1347'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Copy the framework&#39;s dylib into the virtual</span></div><div class='line' id='LC1348'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># environment</span></div><div class='line' id='LC1349'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">virtual_lib</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;.Python&#39;</span><span class="p">)</span></div><div class='line' id='LC1350'><br/></div><div class='line' id='LC1351'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">virtual_lib</span><span class="p">):</span></div><div class='line' id='LC1352'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">unlink</span><span class="p">(</span><span class="n">virtual_lib</span><span class="p">)</span></div><div class='line' id='LC1353'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span></div><div class='line' id='LC1354'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="s">&#39;Python&#39;</span><span class="p">),</span></div><div class='line' id='LC1355'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">virtual_lib</span><span class="p">,</span></div><div class='line' id='LC1356'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1357'><br/></div><div class='line' id='LC1358'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># And then change the install_name of the copied python executable</span></div><div class='line' id='LC1359'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC1360'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mach_o_change</span><span class="p">(</span><span class="n">py_executable</span><span class="p">,</span></div><div class='line' id='LC1361'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="s">&#39;Python&#39;</span><span class="p">),</span></div><div class='line' id='LC1362'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;@executable_path/../.Python&#39;</span><span class="p">)</span></div><div class='line' id='LC1363'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC1364'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">e</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC1365'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&quot;Could not call mach_o_change: </span><span class="si">%s</span><span class="s">. &quot;</span></div><div class='line' id='LC1366'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Trying to call install_name_tool instead.&quot;</span> <span class="o">%</span> <span class="n">e</span><span class="p">)</span></div><div class='line' id='LC1367'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC1368'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">call_subprocess</span><span class="p">(</span></div><div class='line' id='LC1369'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">[</span><span class="s">&quot;install_name_tool&quot;</span><span class="p">,</span> <span class="s">&quot;-change&quot;</span><span class="p">,</span></div><div class='line' id='LC1370'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="s">&#39;Python&#39;</span><span class="p">),</span></div><div class='line' id='LC1371'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;@executable_path/../.Python&#39;</span><span class="p">,</span></div><div class='line' id='LC1372'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_executable</span><span class="p">])</span></div><div class='line' id='LC1373'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC1374'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span><span class="s">&quot;Could not call install_name_tool -- you must &quot;</span></div><div class='line' id='LC1375'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;have Apple&#39;s development tools installed&quot;</span><span class="p">)</span></div><div class='line' id='LC1376'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span></div><div class='line' id='LC1377'><br/></div><div class='line' id='LC1378'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">is_win</span><span class="p">:</span></div><div class='line' id='LC1379'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Ensure that &#39;python&#39;, &#39;pythonX&#39; and &#39;pythonX.Y&#39; all exist</span></div><div class='line' id='LC1380'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_exe_version_major</span> <span class="o">=</span> <span class="s">&#39;python</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC1381'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_exe_version_major_minor</span> <span class="o">=</span> <span class="s">&#39;python</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span></div><div class='line' id='LC1382'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC1383'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_exe_no_version</span> <span class="o">=</span> <span class="s">&#39;python&#39;</span></div><div class='line' id='LC1384'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">required_symlinks</span> <span class="o">=</span> <span class="p">[</span> <span class="n">py_exe_no_version</span><span class="p">,</span> <span class="n">py_exe_version_major</span><span class="p">,</span></div><div class='line' id='LC1385'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_exe_version_major_minor</span> <span class="p">]</span></div><div class='line' id='LC1386'><br/></div><div class='line' id='LC1387'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_executable_base</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">py_executable</span><span class="p">)</span></div><div class='line' id='LC1388'><br/></div><div class='line' id='LC1389'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">py_executable_base</span> <span class="ow">in</span> <span class="n">required_symlinks</span><span class="p">:</span></div><div class='line' id='LC1390'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Don&#39;t try to symlink to yourself.</span></div><div class='line' id='LC1391'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">required_symlinks</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">py_executable_base</span><span class="p">)</span></div><div class='line' id='LC1392'><br/></div><div class='line' id='LC1393'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">pth</span> <span class="ow">in</span> <span class="n">required_symlinks</span><span class="p">:</span></div><div class='line' id='LC1394'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">full_pth</span> <span class="o">=</span> <span class="n">join</span><span class="p">(</span><span class="n">bin_dir</span><span class="p">,</span> <span class="n">pth</span><span class="p">)</span></div><div class='line' id='LC1395'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">full_pth</span><span class="p">):</span></div><div class='line' id='LC1396'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">unlink</span><span class="p">(</span><span class="n">full_pth</span><span class="p">)</span></div><div class='line' id='LC1397'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">symlink</span><span class="p">:</span></div><div class='line' id='LC1398'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">symlink</span><span class="p">(</span><span class="n">py_executable_base</span><span class="p">,</span> <span class="n">full_pth</span><span class="p">)</span></div><div class='line' id='LC1399'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1400'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span><span class="n">py_executable</span><span class="p">,</span> <span class="n">full_pth</span><span class="p">,</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1401'><br/></div><div class='line' id='LC1402'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_win</span> <span class="ow">and</span> <span class="s">&#39; &#39;</span> <span class="ow">in</span> <span class="n">py_executable</span><span class="p">:</span></div><div class='line' id='LC1403'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># There&#39;s a bug with subprocess on Windows when using a first</span></div><div class='line' id='LC1404'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># argument that has a space in it.  Instead we have to quote</span></div><div class='line' id='LC1405'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># the value:</span></div><div class='line' id='LC1406'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_executable</span> <span class="o">=</span> <span class="s">&#39;&quot;</span><span class="si">%s</span><span class="s">&quot;&#39;</span> <span class="o">%</span> <span class="n">py_executable</span></div><div class='line' id='LC1407'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># NOTE: keep this check as one line, cmd.exe doesn&#39;t cope with line breaks</span></div><div class='line' id='LC1408'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cmd</span> <span class="o">=</span> <span class="p">[</span><span class="n">py_executable</span><span class="p">,</span> <span class="s">&#39;-c&#39;</span><span class="p">,</span> <span class="s">&#39;import sys;out=sys.stdout;&#39;</span></div><div class='line' id='LC1409'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;getattr(out, &quot;buffer&quot;, out).write(sys.prefix.encode(&quot;utf-8&quot;))&#39;</span><span class="p">]</span></div><div class='line' id='LC1410'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Testing executable with </span><span class="si">%s</span><span class="s"> </span><span class="si">%s</span><span class="s"> &quot;</span><span class="si">%s</span><span class="s">&quot;&#39;</span> <span class="o">%</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">cmd</span><span class="p">))</span></div><div class='line' id='LC1411'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC1412'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">proc</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">(</span><span class="n">cmd</span><span class="p">,</span></div><div class='line' id='LC1413'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stdout</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">)</span></div><div class='line' id='LC1414'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">proc_stdout</span><span class="p">,</span> <span class="n">proc_stderr</span> <span class="o">=</span> <span class="n">proc</span><span class="o">.</span><span class="n">communicate</span><span class="p">()</span></div><div class='line' id='LC1415'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span></div><div class='line' id='LC1416'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">e</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC1417'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">e</span><span class="o">.</span><span class="n">errno</span> <span class="o">==</span> <span class="n">errno</span><span class="o">.</span><span class="n">EACCES</span><span class="p">:</span></div><div class='line' id='LC1418'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span><span class="s">&#39;ERROR: The executable </span><span class="si">%s</span><span class="s"> could not be run: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">py_executable</span><span class="p">,</span> <span class="n">e</span><span class="p">))</span></div><div class='line' id='LC1419'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">100</span><span class="p">)</span></div><div class='line' id='LC1420'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1421'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">e</span></div><div class='line' id='LC1422'><br/></div><div class='line' id='LC1423'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">proc_stdout</span> <span class="o">=</span> <span class="n">proc_stdout</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s">&quot;utf-8&quot;</span><span class="p">)</span></div><div class='line' id='LC1424'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">proc_stdout</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normcase</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">proc_stdout</span><span class="p">))</span></div><div class='line' id='LC1425'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">norm_home_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normcase</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">home_dir</span><span class="p">))</span></div><div class='line' id='LC1426'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">norm_home_dir</span><span class="p">,</span> <span class="s">&#39;decode&#39;</span><span class="p">):</span></div><div class='line' id='LC1427'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">norm_home_dir</span> <span class="o">=</span> <span class="n">norm_home_dir</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getfilesystemencoding</span><span class="p">())</span></div><div class='line' id='LC1428'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">proc_stdout</span> <span class="o">!=</span> <span class="n">norm_home_dir</span><span class="p">:</span></div><div class='line' id='LC1429'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span></div><div class='line' id='LC1430'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;ERROR: The executable </span><span class="si">%s</span><span class="s"> is not functioning&#39;</span> <span class="o">%</span> <span class="n">py_executable</span><span class="p">)</span></div><div class='line' id='LC1431'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span></div><div class='line' id='LC1432'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;ERROR: It thinks sys.prefix is </span><span class="si">%r</span><span class="s"> (should be </span><span class="si">%r</span><span class="s">)&#39;</span></div><div class='line' id='LC1433'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">%</span> <span class="p">(</span><span class="n">proc_stdout</span><span class="p">,</span> <span class="n">norm_home_dir</span><span class="p">))</span></div><div class='line' id='LC1434'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span></div><div class='line' id='LC1435'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;ERROR: virtualenv is not compatible with this system or executable&#39;</span><span class="p">)</span></div><div class='line' id='LC1436'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_win</span><span class="p">:</span></div><div class='line' id='LC1437'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span></div><div class='line' id='LC1438'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;Note: some Windows users have reported this error when they &#39;</span></div><div class='line' id='LC1439'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;installed Python for &quot;Only this user&quot; or have multiple &#39;</span></div><div class='line' id='LC1440'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;versions of Python installed. Copying the appropriate &#39;</span></div><div class='line' id='LC1441'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;PythonXX.dll to the virtualenv Scripts/ directory may fix &#39;</span></div><div class='line' id='LC1442'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;this problem.&#39;</span><span class="p">)</span></div><div class='line' id='LC1443'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">100</span><span class="p">)</span></div><div class='line' id='LC1444'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1445'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Got sys.prefix result: </span><span class="si">%r</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">proc_stdout</span><span class="p">)</span></div><div class='line' id='LC1446'><br/></div><div class='line' id='LC1447'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pydistutils</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">expanduser</span><span class="p">(</span><span class="s">&#39;~/.pydistutils.cfg&#39;</span><span class="p">)</span></div><div class='line' id='LC1448'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">pydistutils</span><span class="p">):</span></div><div class='line' id='LC1449'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Please make sure you remove any previous custom paths from &#39;</span></div><div class='line' id='LC1450'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;your </span><span class="si">%s</span><span class="s"> file.&#39;</span> <span class="o">%</span> <span class="n">pydistutils</span><span class="p">)</span></div><div class='line' id='LC1451'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">## FIXME: really this should be calculated earlier</span></div><div class='line' id='LC1452'><br/></div><div class='line' id='LC1453'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fix_local_scheme</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1454'><br/></div><div class='line' id='LC1455'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">site_packages</span><span class="p">:</span></div><div class='line' id='LC1456'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">site_packages_filename</span><span class="p">):</span></div><div class='line' id='LC1457'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Deleting </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">site_packages_filename</span><span class="p">)</span></div><div class='line' id='LC1458'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">unlink</span><span class="p">(</span><span class="n">site_packages_filename</span><span class="p">)</span></div><div class='line' id='LC1459'><br/></div><div class='line' id='LC1460'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">py_executable</span></div><div class='line' id='LC1461'><br/></div><div class='line' id='LC1462'><br/></div><div class='line' id='LC1463'><span class="k">def</span> <span class="nf">install_activate</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="n">bin_dir</span><span class="p">,</span> <span class="n">prompt</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC1464'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">home_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC1465'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_win</span> <span class="ow">or</span> <span class="n">is_jython</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">_name</span> <span class="o">==</span> <span class="s">&#39;nt&#39;</span><span class="p">:</span></div><div class='line' id='LC1466'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC1467'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;activate.bat&#39;</span><span class="p">:</span> <span class="n">ACTIVATE_BAT</span><span class="p">,</span></div><div class='line' id='LC1468'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;deactivate.bat&#39;</span><span class="p">:</span> <span class="n">DEACTIVATE_BAT</span><span class="p">,</span></div><div class='line' id='LC1469'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;activate.ps1&#39;</span><span class="p">:</span> <span class="n">ACTIVATE_PS</span><span class="p">,</span></div><div class='line' id='LC1470'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC1471'><br/></div><div class='line' id='LC1472'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># MSYS needs paths of the form /c/path/to/file</span></div><div class='line' id='LC1473'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">drive</span><span class="p">,</span> <span class="n">tail</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitdrive</span><span class="p">(</span><span class="n">home_dir</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">sep</span><span class="p">,</span> <span class="s">&#39;/&#39;</span><span class="p">))</span></div><div class='line' id='LC1474'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">home_dir_msys</span> <span class="o">=</span> <span class="p">(</span><span class="n">drive</span> <span class="ow">and</span> <span class="s">&quot;/</span><span class="si">%s%s</span><span class="s">&quot;</span> <span class="ow">or</span> <span class="s">&quot;</span><span class="si">%s%s</span><span class="s">&quot;</span><span class="p">)</span> <span class="o">%</span> <span class="p">(</span><span class="n">drive</span><span class="p">[:</span><span class="mi">1</span><span class="p">],</span> <span class="n">tail</span><span class="p">)</span></div><div class='line' id='LC1475'><br/></div><div class='line' id='LC1476'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Run-time conditional enables (basic) Cygwin compatibility</span></div><div class='line' id='LC1477'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">home_dir_sh</span> <span class="o">=</span> <span class="p">(</span><span class="s">&quot;&quot;&quot;$(if [ &quot;$OSTYPE&quot; &quot;==&quot; &quot;cygwin&quot; ]; then cygpath -u &#39;</span><span class="si">%s</span><span class="s">&#39;; else echo &#39;</span><span class="si">%s</span><span class="s">&#39;; fi;)&quot;&quot;&quot;</span> <span class="o">%</span></div><div class='line' id='LC1478'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="n">home_dir_msys</span><span class="p">))</span></div><div class='line' id='LC1479'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span><span class="p">[</span><span class="s">&#39;activate&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">ACTIVATE_SH</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;__VIRTUAL_ENV__&#39;</span><span class="p">,</span> <span class="n">home_dir_sh</span><span class="p">)</span></div><div class='line' id='LC1480'><br/></div><div class='line' id='LC1481'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1482'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;activate&#39;</span><span class="p">:</span> <span class="n">ACTIVATE_SH</span><span class="p">}</span></div><div class='line' id='LC1483'><br/></div><div class='line' id='LC1484'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># suppling activate.fish in addition to, not instead of, the</span></div><div class='line' id='LC1485'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># bash script support.</span></div><div class='line' id='LC1486'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span><span class="p">[</span><span class="s">&#39;activate.fish&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">ACTIVATE_FISH</span></div><div class='line' id='LC1487'><br/></div><div class='line' id='LC1488'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># same for csh/tcsh support...</span></div><div class='line' id='LC1489'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span><span class="p">[</span><span class="s">&#39;activate.csh&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">ACTIVATE_CSH</span></div><div class='line' id='LC1490'><br/></div><div class='line' id='LC1491'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span><span class="p">[</span><span class="s">&#39;activate_this.py&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">ACTIVATE_THIS</span></div><div class='line' id='LC1492'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;decode&#39;</span><span class="p">):</span></div><div class='line' id='LC1493'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">home_dir</span> <span class="o">=</span> <span class="n">home_dir</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getfilesystemencoding</span><span class="p">())</span></div><div class='line' id='LC1494'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">vname</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC1495'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">content</span> <span class="ow">in</span> <span class="n">files</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></div><div class='line' id='LC1496'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">content</span> <span class="o">=</span> <span class="n">content</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;__VIRTUAL_PROMPT__&#39;</span><span class="p">,</span> <span class="n">prompt</span> <span class="ow">or</span> <span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC1497'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">content</span> <span class="o">=</span> <span class="n">content</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;__VIRTUAL_WINPROMPT__&#39;</span><span class="p">,</span> <span class="n">prompt</span> <span class="ow">or</span> <span class="s">&#39;(</span><span class="si">%s</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="n">vname</span><span class="p">)</span></div><div class='line' id='LC1498'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">content</span> <span class="o">=</span> <span class="n">content</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;__VIRTUAL_ENV__&#39;</span><span class="p">,</span> <span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC1499'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">content</span> <span class="o">=</span> <span class="n">content</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;__VIRTUAL_NAME__&#39;</span><span class="p">,</span> <span class="n">vname</span><span class="p">)</span></div><div class='line' id='LC1500'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">content</span> <span class="o">=</span> <span class="n">content</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;__BIN_NAME__&#39;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">bin_dir</span><span class="p">))</span></div><div class='line' id='LC1501'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writefile</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">bin_dir</span><span class="p">,</span> <span class="n">name</span><span class="p">),</span> <span class="n">content</span><span class="p">)</span></div><div class='line' id='LC1502'><br/></div><div class='line' id='LC1503'><span class="k">def</span> <span class="nf">install_distutils</span><span class="p">(</span><span class="n">home_dir</span><span class="p">):</span></div><div class='line' id='LC1504'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">distutils_path</span> <span class="o">=</span> <span class="n">change_prefix</span><span class="p">(</span><span class="n">distutils</span><span class="o">.</span><span class="n">__path__</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC1505'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mkdir</span><span class="p">(</span><span class="n">distutils_path</span><span class="p">)</span></div><div class='line' id='LC1506'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">## FIXME: maybe this prefix setting should only be put in place if</span></div><div class='line' id='LC1507'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">## there&#39;s a local distutils.cfg with a prefix setting?</span></div><div class='line' id='LC1508'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">home_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC1509'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">## FIXME: this is breaking things, removing for now:</span></div><div class='line' id='LC1510'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#distutils_cfg = DISTUTILS_CFG + &quot;\n[install]\nprefix=%s\n&quot; % home_dir</span></div><div class='line' id='LC1511'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writefile</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">distutils_path</span><span class="p">,</span> <span class="s">&#39;__init__.py&#39;</span><span class="p">),</span> <span class="n">DISTUTILS_INIT</span><span class="p">)</span></div><div class='line' id='LC1512'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writefile</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">distutils_path</span><span class="p">,</span> <span class="s">&#39;distutils.cfg&#39;</span><span class="p">),</span> <span class="n">DISTUTILS_CFG</span><span class="p">,</span> <span class="n">overwrite</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC1513'><br/></div><div class='line' id='LC1514'><span class="k">def</span> <span class="nf">fix_local_scheme</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="n">symlink</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></div><div class='line' id='LC1515'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC1516'><span class="sd">    Platforms that use the &quot;posix_local&quot; install scheme (like Ubuntu with</span></div><div class='line' id='LC1517'><span class="sd">    Python 2.7) need to be given an additional &quot;local&quot; location, sigh.</span></div><div class='line' id='LC1518'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC1519'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC1520'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">sysconfig</span></div><div class='line' id='LC1521'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div><div class='line' id='LC1522'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1523'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1524'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">sysconfig</span><span class="o">.</span><span class="n">_get_default_scheme</span><span class="p">()</span> <span class="o">==</span> <span class="s">&#39;posix_local&#39;</span><span class="p">:</span></div><div class='line' id='LC1525'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">local_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="s">&#39;local&#39;</span><span class="p">)</span></div><div class='line' id='LC1526'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">local_path</span><span class="p">):</span></div><div class='line' id='LC1527'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span><span class="n">local_path</span><span class="p">)</span></div><div class='line' id='LC1528'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">subdir_name</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">home_dir</span><span class="p">):</span></div><div class='line' id='LC1529'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">subdir_name</span> <span class="o">==</span> <span class="s">&#39;local&#39;</span><span class="p">:</span></div><div class='line' id='LC1530'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC1531'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copyfile</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="n">subdir_name</span><span class="p">)),</span> \</div><div class='line' id='LC1532'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">local_path</span><span class="p">,</span> <span class="n">subdir_name</span><span class="p">),</span> <span class="n">symlink</span><span class="p">)</span></div><div class='line' id='LC1533'><br/></div><div class='line' id='LC1534'><span class="k">def</span> <span class="nf">fix_lib64</span><span class="p">(</span><span class="n">lib_dir</span><span class="p">,</span> <span class="n">symlink</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></div><div class='line' id='LC1535'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC1536'><span class="sd">    Some platforms (particularly Gentoo on x64) put things in lib64/pythonX.Y</span></div><div class='line' id='LC1537'><span class="sd">    instead of lib/pythonX.Y.  If this is such a platform we&#39;ll just create a</span></div><div class='line' id='LC1538'><span class="sd">    symlink so lib64 points to lib</span></div><div class='line' id='LC1539'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC1540'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">[</span><span class="n">p</span> <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">distutils</span><span class="o">.</span><span class="n">sysconfig</span><span class="o">.</span><span class="n">get_config_vars</span><span class="p">()</span><span class="o">.</span><span class="n">values</span><span class="p">()</span></div><div class='line' id='LC1541'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="nb">basestring</span><span class="p">)</span> <span class="ow">and</span> <span class="s">&#39;lib64&#39;</span> <span class="ow">in</span> <span class="n">p</span><span class="p">]:</span></div><div class='line' id='LC1542'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># PyPy&#39;s library path scheme is not affected by this.</span></div><div class='line' id='LC1543'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Return early or we will die on the following assert.</span></div><div class='line' id='LC1544'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_pypy</span><span class="p">:</span></div><div class='line' id='LC1545'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;PyPy detected, skipping lib64 symlinking&#39;</span><span class="p">)</span></div><div class='line' id='LC1546'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC1547'><br/></div><div class='line' id='LC1548'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;This system uses lib64; symlinking lib64 to lib&#39;</span><span class="p">)</span></div><div class='line' id='LC1549'><br/></div><div class='line' id='LC1550'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">lib_dir</span><span class="p">)</span> <span class="o">==</span> <span class="s">&#39;python</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">sys</span><span class="o">.</span><span class="n">version</span><span class="p">[:</span><span class="mi">3</span><span class="p">],</span> <span class="p">(</span></div><div class='line' id='LC1551'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Unexpected python lib dir: </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">lib_dir</span><span class="p">)</span></div><div class='line' id='LC1552'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lib_parent</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">lib_dir</span><span class="p">)</span></div><div class='line' id='LC1553'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">top_level</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">lib_parent</span><span class="p">)</span></div><div class='line' id='LC1554'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lib_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">top_level</span><span class="p">,</span> <span class="s">&#39;lib&#39;</span><span class="p">)</span></div><div class='line' id='LC1555'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lib64_link</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">top_level</span><span class="p">,</span> <span class="s">&#39;lib64&#39;</span><span class="p">)</span></div><div class='line' id='LC1556'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">lib_parent</span><span class="p">)</span> <span class="o">==</span> <span class="s">&#39;lib&#39;</span><span class="p">,</span> <span class="p">(</span></div><div class='line' id='LC1557'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Unexpected parent dir: </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">lib_parent</span><span class="p">)</span></div><div class='line' id='LC1558'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">lexists</span><span class="p">(</span><span class="n">lib64_link</span><span class="p">):</span></div><div class='line' id='LC1559'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC1560'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cp_or_ln</span> <span class="o">=</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">symlink</span> <span class="k">if</span> <span class="n">symlink</span> <span class="k">else</span> <span class="n">copyfile</span><span class="p">)</span></div><div class='line' id='LC1561'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cp_or_ln</span><span class="p">(</span><span class="s">&#39;lib&#39;</span><span class="p">,</span> <span class="n">lib64_link</span><span class="p">)</span></div><div class='line' id='LC1562'><br/></div><div class='line' id='LC1563'><span class="k">def</span> <span class="nf">resolve_interpreter</span><span class="p">(</span><span class="n">exe</span><span class="p">):</span></div><div class='line' id='LC1564'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC1565'><span class="sd">    If the executable given isn&#39;t an absolute path, search $PATH for the interpreter</span></div><div class='line' id='LC1566'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC1567'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># If the &quot;executable&quot; is a version number, get the installed executable for</span></div><div class='line' id='LC1568'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># that version</span></div><div class='line' id='LC1569'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">python_versions</span> <span class="o">=</span> <span class="n">get_installed_pythons</span><span class="p">()</span></div><div class='line' id='LC1570'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">exe</span> <span class="ow">in</span> <span class="n">python_versions</span><span class="p">:</span></div><div class='line' id='LC1571'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">exe</span> <span class="o">=</span> <span class="n">python_versions</span><span class="p">[</span><span class="n">exe</span><span class="p">]</span></div><div class='line' id='LC1572'><br/></div><div class='line' id='LC1573'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">exe</span><span class="p">)</span> <span class="o">!=</span> <span class="n">exe</span><span class="p">:</span></div><div class='line' id='LC1574'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">paths</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;PATH&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">pathsep</span><span class="p">)</span></div><div class='line' id='LC1575'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="n">paths</span><span class="p">:</span></div><div class='line' id='LC1576'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">exe</span><span class="p">)):</span></div><div class='line' id='LC1577'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">exe</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">exe</span><span class="p">)</span></div><div class='line' id='LC1578'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC1579'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">exe</span><span class="p">):</span></div><div class='line' id='LC1580'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span><span class="s">&#39;The executable </span><span class="si">%s</span><span class="s"> (from --python=</span><span class="si">%s</span><span class="s">) does not exist&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">exe</span><span class="p">,</span> <span class="n">exe</span><span class="p">))</span></div><div class='line' id='LC1581'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">SystemExit</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span></div><div class='line' id='LC1582'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">is_executable</span><span class="p">(</span><span class="n">exe</span><span class="p">):</span></div><div class='line' id='LC1583'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span><span class="s">&#39;The executable </span><span class="si">%s</span><span class="s"> (from --python=</span><span class="si">%s</span><span class="s">) is not executable&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">exe</span><span class="p">,</span> <span class="n">exe</span><span class="p">))</span></div><div class='line' id='LC1584'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">SystemExit</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span></div><div class='line' id='LC1585'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">exe</span></div><div class='line' id='LC1586'><br/></div><div class='line' id='LC1587'><span class="k">def</span> <span class="nf">is_executable</span><span class="p">(</span><span class="n">exe</span><span class="p">):</span></div><div class='line' id='LC1588'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Checks a file is executable&quot;&quot;&quot;</span></div><div class='line' id='LC1589'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">os</span><span class="o">.</span><span class="n">access</span><span class="p">(</span><span class="n">exe</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">X_OK</span><span class="p">)</span></div><div class='line' id='LC1590'><br/></div><div class='line' id='LC1591'><span class="c">############################################################</span></div><div class='line' id='LC1592'><span class="c">## Relocating the environment:</span></div><div class='line' id='LC1593'><br/></div><div class='line' id='LC1594'><span class="k">def</span> <span class="nf">make_environment_relocatable</span><span class="p">(</span><span class="n">home_dir</span><span class="p">):</span></div><div class='line' id='LC1595'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC1596'><span class="sd">    Makes the already-existing environment use relative paths, and takes out</span></div><div class='line' id='LC1597'><span class="sd">    the #!-based environment selection in scripts.</span></div><div class='line' id='LC1598'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC1599'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">home_dir</span><span class="p">,</span> <span class="n">lib_dir</span><span class="p">,</span> <span class="n">inc_dir</span><span class="p">,</span> <span class="n">bin_dir</span> <span class="o">=</span> <span class="n">path_locations</span><span class="p">(</span><span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC1600'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">activate_this</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">bin_dir</span><span class="p">,</span> <span class="s">&#39;activate_this.py&#39;</span><span class="p">)</span></div><div class='line' id='LC1601'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">activate_this</span><span class="p">):</span></div><div class='line' id='LC1602'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">fatal</span><span class="p">(</span></div><div class='line' id='LC1603'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;The environment doesn</span><span class="se">\&#39;</span><span class="s">t have a file </span><span class="si">%s</span><span class="s"> -- please re-run virtualenv &#39;</span></div><div class='line' id='LC1604'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;on this environment to update it&#39;</span> <span class="o">%</span> <span class="n">activate_this</span><span class="p">)</span></div><div class='line' id='LC1605'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fixup_scripts</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="n">bin_dir</span><span class="p">)</span></div><div class='line' id='LC1606'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fixup_pth_and_egg_link</span><span class="p">(</span><span class="n">home_dir</span><span class="p">)</span></div><div class='line' id='LC1607'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">## FIXME: need to fix up distutils.cfg</span></div><div class='line' id='LC1608'><br/></div><div class='line' id='LC1609'><span class="n">OK_ABS_SCRIPTS</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;python&#39;</span><span class="p">,</span> <span class="s">&#39;python</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">sys</span><span class="o">.</span><span class="n">version</span><span class="p">[:</span><span class="mi">3</span><span class="p">],</span></div><div class='line' id='LC1610'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;activate&#39;</span><span class="p">,</span> <span class="s">&#39;activate.bat&#39;</span><span class="p">,</span> <span class="s">&#39;activate_this.py&#39;</span><span class="p">,</span></div><div class='line' id='LC1611'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;activate.fish&#39;</span><span class="p">,</span> <span class="s">&#39;activate.csh&#39;</span><span class="p">]</span></div><div class='line' id='LC1612'><br/></div><div class='line' id='LC1613'><span class="k">def</span> <span class="nf">fixup_scripts</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="n">bin_dir</span><span class="p">):</span></div><div class='line' id='LC1614'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">is_win</span><span class="p">:</span></div><div class='line' id='LC1615'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">new_shebang_args</span> <span class="o">=</span> <span class="p">(</span></div><div class='line' id='LC1616'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;</span><span class="si">%s</span><span class="s"> /c&#39;</span> <span class="o">%</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normcase</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;COMSPEC&#39;</span><span class="p">,</span> <span class="s">&#39;cmd.exe&#39;</span><span class="p">)),</span></div><div class='line' id='LC1617'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;&#39;</span><span class="p">,</span> <span class="s">&#39;.exe&#39;</span><span class="p">)</span></div><div class='line' id='LC1618'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1619'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">new_shebang_args</span> <span class="o">=</span> <span class="p">(</span><span class="s">&#39;/usr/bin/env&#39;</span><span class="p">,</span> <span class="n">sys</span><span class="o">.</span><span class="n">version</span><span class="p">[:</span><span class="mi">3</span><span class="p">],</span> <span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC1620'><br/></div><div class='line' id='LC1621'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># This is what we expect at the top of scripts:</span></div><div class='line' id='LC1622'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shebang</span> <span class="o">=</span> <span class="s">&#39;#!</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normcase</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span></div><div class='line' id='LC1623'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">bin_dir</span><span class="p">),</span> <span class="s">&#39;python</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">new_shebang_args</span><span class="p">[</span><span class="mi">2</span><span class="p">]))</span></div><div class='line' id='LC1624'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># This is what we&#39;ll put:</span></div><div class='line' id='LC1625'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">new_shebang</span> <span class="o">=</span> <span class="s">&#39;#!</span><span class="si">%s</span><span class="s"> python</span><span class="si">%s%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">new_shebang_args</span></div><div class='line' id='LC1626'><br/></div><div class='line' id='LC1627'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">filename</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">bin_dir</span><span class="p">):</span></div><div class='line' id='LC1628'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">bin_dir</span><span class="p">,</span> <span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1629'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span></div><div class='line' id='LC1630'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># ignore subdirs, e.g. .svn ones.</span></div><div class='line' id='LC1631'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC1632'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="s">&#39;rb&#39;</span><span class="p">)</span></div><div class='line' id='LC1633'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC1634'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC1635'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lines</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s">&#39;utf-8&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()</span></div><div class='line' id='LC1636'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">UnicodeDecodeError</span><span class="p">:</span></div><div class='line' id='LC1637'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># This is probably a binary program instead</span></div><div class='line' id='LC1638'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># of a script, so just ignore it.</span></div><div class='line' id='LC1639'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC1640'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">finally</span><span class="p">:</span></div><div class='line' id='LC1641'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC1642'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">lines</span><span class="p">:</span></div><div class='line' id='LC1643'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&#39;Script </span><span class="si">%s</span><span class="s"> is an empty file&#39;</span> <span class="o">%</span> <span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1644'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC1645'><br/></div><div class='line' id='LC1646'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">old_shebang</span> <span class="o">=</span> <span class="n">lines</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC1647'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">old_shebang</span> <span class="o">=</span> <span class="n">old_shebang</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">2</span><span class="p">]</span> <span class="o">+</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normcase</span><span class="p">(</span><span class="n">old_shebang</span><span class="p">[</span><span class="mi">2</span><span class="p">:])</span></div><div class='line' id='LC1648'><br/></div><div class='line' id='LC1649'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">old_shebang</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">shebang</span><span class="p">):</span></div><div class='line' id='LC1650'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span> <span class="ow">in</span> <span class="n">OK_ABS_SCRIPTS</span><span class="p">:</span></div><div class='line' id='LC1651'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;Cannot make script </span><span class="si">%s</span><span class="s"> relative&#39;</span> <span class="o">%</span> <span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1652'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">lines</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="o">==</span> <span class="n">new_shebang</span><span class="p">:</span></div><div class='line' id='LC1653'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Script </span><span class="si">%s</span><span class="s"> has already been made relative&#39;</span> <span class="o">%</span> <span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1654'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1655'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&#39;Script </span><span class="si">%s</span><span class="s"> cannot be made relative (it</span><span class="se">\&#39;</span><span class="s">s not a normal script that starts with </span><span class="si">%s</span><span class="s">)&#39;</span></div><div class='line' id='LC1656'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">%</span> <span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">shebang</span><span class="p">))</span></div><div class='line' id='LC1657'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC1658'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Making script </span><span class="si">%s</span><span class="s"> relative&#39;</span> <span class="o">%</span> <span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1659'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">script</span> <span class="o">=</span> <span class="n">relative_script</span><span class="p">([</span><span class="n">new_shebang</span><span class="p">]</span> <span class="o">+</span> <span class="n">lines</span><span class="p">[</span><span class="mi">1</span><span class="p">:])</span></div><div class='line' id='LC1660'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="s">&#39;wb&#39;</span><span class="p">)</span></div><div class='line' id='LC1661'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">script</span><span class="p">)</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&#39;utf-8&#39;</span><span class="p">))</span></div><div class='line' id='LC1662'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC1663'><br/></div><div class='line' id='LC1664'><span class="k">def</span> <span class="nf">relative_script</span><span class="p">(</span><span class="n">lines</span><span class="p">):</span></div><div class='line' id='LC1665'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Return a script that&#39;ll work in a relocatable environment.&quot;</span></div><div class='line' id='LC1666'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">activate</span> <span class="o">=</span> <span class="s">&quot;import os; activate_this=os.path.join(os.path.dirname(os.path.realpath(__file__)), &#39;activate_this.py&#39;); exec(compile(open(activate_this).read(), activate_this, &#39;exec&#39;), dict(__file__=activate_this)); del os, activate_this&quot;</span></div><div class='line' id='LC1667'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Find the last future statement in the script. If we insert the activation</span></div><div class='line' id='LC1668'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># line before a future statement, Python will raise a SyntaxError.</span></div><div class='line' id='LC1669'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">activate_at</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC1670'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">line</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="nb">enumerate</span><span class="p">(</span><span class="n">lines</span><span class="p">))):</span></div><div class='line' id='LC1671'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()[:</span><span class="mi">3</span><span class="p">]</span> <span class="o">==</span> <span class="p">[</span><span class="s">&#39;from&#39;</span><span class="p">,</span> <span class="s">&#39;__future__&#39;</span><span class="p">,</span> <span class="s">&#39;import&#39;</span><span class="p">]:</span></div><div class='line' id='LC1672'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">activate_at</span> <span class="o">=</span> <span class="n">idx</span> <span class="o">+</span> <span class="mi">1</span></div><div class='line' id='LC1673'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC1674'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">activate_at</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC1675'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Activate after the shebang.</span></div><div class='line' id='LC1676'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">activate_at</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC1677'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">lines</span><span class="p">[:</span><span class="n">activate_at</span><span class="p">]</span> <span class="o">+</span> <span class="p">[</span><span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">activate</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="n">lines</span><span class="p">[</span><span class="n">activate_at</span><span class="p">:]</span></div><div class='line' id='LC1678'><br/></div><div class='line' id='LC1679'><span class="k">def</span> <span class="nf">fixup_pth_and_egg_link</span><span class="p">(</span><span class="n">home_dir</span><span class="p">,</span> <span class="n">sys_path</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC1680'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Makes .pth and .egg-link files use relative paths&quot;&quot;&quot;</span></div><div class='line' id='LC1681'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">home_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normcase</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">home_dir</span><span class="p">))</span></div><div class='line' id='LC1682'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">sys_path</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC1683'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys_path</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">path</span></div><div class='line' id='LC1684'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="n">sys_path</span><span class="p">:</span></div><div class='line' id='LC1685'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">path</span><span class="p">:</span></div><div class='line' id='LC1686'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">path</span> <span class="o">=</span> <span class="s">&#39;.&#39;</span></div><div class='line' id='LC1687'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="n">path</span><span class="p">):</span></div><div class='line' id='LC1688'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC1689'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normcase</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">path</span><span class="p">))</span></div><div class='line' id='LC1690'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">path</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">home_dir</span><span class="p">):</span></div><div class='line' id='LC1691'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;Skipping system (non-environment) directory </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">path</span><span class="p">)</span></div><div class='line' id='LC1692'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC1693'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">filename</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">path</span><span class="p">):</span></div><div class='line' id='LC1694'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1695'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;.pth&#39;</span><span class="p">):</span></div><div class='line' id='LC1696'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">access</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">W_OK</span><span class="p">):</span></div><div class='line' id='LC1697'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&#39;Cannot write .pth file </span><span class="si">%s</span><span class="s">, skipping&#39;</span> <span class="o">%</span> <span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1698'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1699'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fixup_pth_file</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1700'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;.egg-link&#39;</span><span class="p">):</span></div><div class='line' id='LC1701'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">access</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">W_OK</span><span class="p">):</span></div><div class='line' id='LC1702'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&#39;Cannot write .egg-link file </span><span class="si">%s</span><span class="s">, skipping&#39;</span> <span class="o">%</span> <span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1703'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1704'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fixup_egg_link</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1705'><br/></div><div class='line' id='LC1706'><span class="k">def</span> <span class="nf">fixup_pth_file</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span></div><div class='line' id='LC1707'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lines</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC1708'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prev_lines</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC1709'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1710'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prev_lines</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">readlines</span><span class="p">()</span></div><div class='line' id='LC1711'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC1712'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">prev_lines</span><span class="p">:</span></div><div class='line' id='LC1713'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">line</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC1714'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">line</span> <span class="ow">or</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;#&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;import &#39;</span><span class="p">)</span></div><div class='line' id='LC1715'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">line</span><span class="p">)</span> <span class="o">!=</span> <span class="n">line</span><span class="p">):</span></div><div class='line' id='LC1716'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="p">)</span></div><div class='line' id='LC1717'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC1718'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">new_value</span> <span class="o">=</span> <span class="n">make_relative_path</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">line</span><span class="p">)</span></div><div class='line' id='LC1719'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">line</span> <span class="o">!=</span> <span class="n">new_value</span><span class="p">:</span></div><div class='line' id='LC1720'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;Rewriting path </span><span class="si">%s</span><span class="s"> as </span><span class="si">%s</span><span class="s"> (in </span><span class="si">%s</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">line</span><span class="p">,</span> <span class="n">new_value</span><span class="p">,</span> <span class="n">filename</span><span class="p">))</span></div><div class='line' id='LC1721'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">new_value</span><span class="p">)</span></div><div class='line' id='LC1722'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">lines</span> <span class="o">==</span> <span class="n">prev_lines</span><span class="p">:</span></div><div class='line' id='LC1723'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;No changes to .pth file </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1724'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC1725'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Making paths in .pth file </span><span class="si">%s</span><span class="s"> relative&#39;</span> <span class="o">%</span> <span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1726'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span></div><div class='line' id='LC1727'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lines</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC1728'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC1729'><br/></div><div class='line' id='LC1730'><span class="k">def</span> <span class="nf">fixup_egg_link</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span></div><div class='line' id='LC1731'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1732'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">link</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC1733'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC1734'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">link</span><span class="p">)</span> <span class="o">!=</span> <span class="n">link</span><span class="p">:</span></div><div class='line' id='LC1735'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;Link in </span><span class="si">%s</span><span class="s"> already relative&#39;</span> <span class="o">%</span> <span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC1736'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC1737'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">new_link</span> <span class="o">=</span> <span class="n">make_relative_path</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">link</span><span class="p">)</span></div><div class='line' id='LC1738'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">notify</span><span class="p">(</span><span class="s">&#39;Rewriting link </span><span class="si">%s</span><span class="s"> in </span><span class="si">%s</span><span class="s"> as </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">link</span><span class="p">,</span> <span class="n">filename</span><span class="p">,</span> <span class="n">new_link</span><span class="p">))</span></div><div class='line' id='LC1739'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span></div><div class='line' id='LC1740'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">new_link</span><span class="p">)</span></div><div class='line' id='LC1741'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC1742'><br/></div><div class='line' id='LC1743'><span class="k">def</span> <span class="nf">make_relative_path</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">dest</span><span class="p">,</span> <span class="n">dest_is_directory</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></div><div class='line' id='LC1744'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC1745'><span class="sd">    Make a filename relative, where the filename is dest, and it is</span></div><div class='line' id='LC1746'><span class="sd">    being referred to from the filename source.</span></div><div class='line' id='LC1747'><br/></div><div class='line' id='LC1748'><span class="sd">        &gt;&gt;&gt; make_relative_path(&#39;/usr/share/something/a-file.pth&#39;,</span></div><div class='line' id='LC1749'><span class="sd">        ...                    &#39;/usr/share/another-place/src/Directory&#39;)</span></div><div class='line' id='LC1750'><span class="sd">        &#39;../another-place/src/Directory&#39;</span></div><div class='line' id='LC1751'><span class="sd">        &gt;&gt;&gt; make_relative_path(&#39;/usr/share/something/a-file.pth&#39;,</span></div><div class='line' id='LC1752'><span class="sd">        ...                    &#39;/home/user/src/Directory&#39;)</span></div><div class='line' id='LC1753'><span class="sd">        &#39;../../../home/user/src/Directory&#39;</span></div><div class='line' id='LC1754'><span class="sd">        &gt;&gt;&gt; make_relative_path(&#39;/usr/share/a-file.pth&#39;, &#39;/usr/share/&#39;)</span></div><div class='line' id='LC1755'><span class="sd">        &#39;./&#39;</span></div><div class='line' id='LC1756'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC1757'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">source</span><span class="p">)</span></div><div class='line' id='LC1758'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">dest_is_directory</span><span class="p">:</span></div><div class='line' id='LC1759'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest_filename</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC1760'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">dest</span><span class="p">)</span></div><div class='line' id='LC1761'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normpath</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">dest</span><span class="p">))</span></div><div class='line' id='LC1762'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normpath</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">source</span><span class="p">))</span></div><div class='line' id='LC1763'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest_parts</span> <span class="o">=</span> <span class="n">dest</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">sep</span><span class="p">)</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">sep</span><span class="p">)</span></div><div class='line' id='LC1764'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source_parts</span> <span class="o">=</span> <span class="n">source</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">sep</span><span class="p">)</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">sep</span><span class="p">)</span></div><div class='line' id='LC1765'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="n">dest_parts</span> <span class="ow">and</span> <span class="n">source_parts</span> <span class="ow">and</span> <span class="n">dest_parts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="n">source_parts</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span></div><div class='line' id='LC1766'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest_parts</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC1767'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">source_parts</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC1768'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">full_parts</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;..&#39;</span><span class="p">]</span><span class="o">*</span><span class="nb">len</span><span class="p">(</span><span class="n">source_parts</span><span class="p">)</span> <span class="o">+</span> <span class="n">dest_parts</span></div><div class='line' id='LC1769'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">dest_is_directory</span><span class="p">:</span></div><div class='line' id='LC1770'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">full_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">dest_filename</span><span class="p">)</span></div><div class='line' id='LC1771'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">full_parts</span><span class="p">:</span></div><div class='line' id='LC1772'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Special case for the current directory (otherwise it&#39;d be &#39;&#39;)</span></div><div class='line' id='LC1773'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;./&#39;</span></div><div class='line' id='LC1774'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">sep</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">full_parts</span><span class="p">)</span></div><div class='line' id='LC1775'><br/></div><div class='line' id='LC1776'><br/></div><div class='line' id='LC1777'><br/></div><div class='line' id='LC1778'><span class="c">############################################################</span></div><div class='line' id='LC1779'><span class="c">## Bootstrap script creation:</span></div><div class='line' id='LC1780'><br/></div><div class='line' id='LC1781'><span class="k">def</span> <span class="nf">create_bootstrap_script</span><span class="p">(</span><span class="n">extra_text</span><span class="p">,</span> <span class="n">python_version</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span></div><div class='line' id='LC1782'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC1783'><span class="sd">    Creates a bootstrap script, which is like this script but with</span></div><div class='line' id='LC1784'><span class="sd">    extend_parser, adjust_options, and after_install hooks.</span></div><div class='line' id='LC1785'><br/></div><div class='line' id='LC1786'><span class="sd">    This returns a string that (written to disk of course) can be used</span></div><div class='line' id='LC1787'><span class="sd">    as a bootstrap script with your own customizations.  The script</span></div><div class='line' id='LC1788'><span class="sd">    will be the standard virtualenv.py script, with your extra text</span></div><div class='line' id='LC1789'><span class="sd">    added (your extra text should be Python code).</span></div><div class='line' id='LC1790'><br/></div><div class='line' id='LC1791'><span class="sd">    If you include these functions, they will be called:</span></div><div class='line' id='LC1792'><br/></div><div class='line' id='LC1793'><span class="sd">    ``extend_parser(optparse_parser)``:</span></div><div class='line' id='LC1794'><span class="sd">        You can add or remove options from the parser here.</span></div><div class='line' id='LC1795'><br/></div><div class='line' id='LC1796'><span class="sd">    ``adjust_options(options, args)``:</span></div><div class='line' id='LC1797'><span class="sd">        You can change options here, or change the args (if you accept</span></div><div class='line' id='LC1798'><span class="sd">        different kinds of arguments, be sure you modify ``args`` so it is</span></div><div class='line' id='LC1799'><span class="sd">        only ``[DEST_DIR]``).</span></div><div class='line' id='LC1800'><br/></div><div class='line' id='LC1801'><span class="sd">    ``after_install(options, home_dir)``:</span></div><div class='line' id='LC1802'><br/></div><div class='line' id='LC1803'><span class="sd">        After everything is installed, this function is called.  This</span></div><div class='line' id='LC1804'><span class="sd">        is probably the function you are most likely to use.  An</span></div><div class='line' id='LC1805'><span class="sd">        example would be::</span></div><div class='line' id='LC1806'><br/></div><div class='line' id='LC1807'><span class="sd">            def after_install(options, home_dir):</span></div><div class='line' id='LC1808'><span class="sd">                subprocess.call([join(home_dir, &#39;bin&#39;, &#39;easy_install&#39;),</span></div><div class='line' id='LC1809'><span class="sd">                                 &#39;MyPackage&#39;])</span></div><div class='line' id='LC1810'><span class="sd">                subprocess.call([join(home_dir, &#39;bin&#39;, &#39;my-package-script&#39;),</span></div><div class='line' id='LC1811'><span class="sd">                                 &#39;setup&#39;, home_dir])</span></div><div class='line' id='LC1812'><br/></div><div class='line' id='LC1813'><span class="sd">        This example immediately installs a package, and runs a setup</span></div><div class='line' id='LC1814'><span class="sd">        script from that package.</span></div><div class='line' id='LC1815'><br/></div><div class='line' id='LC1816'><span class="sd">    If you provide something like ``python_version=&#39;2.5&#39;`` then the</span></div><div class='line' id='LC1817'><span class="sd">    script will start with ``#!/usr/bin/env python2.5`` instead of</span></div><div class='line' id='LC1818'><span class="sd">    ``#!/usr/bin/env python``.  You can use this when the script must</span></div><div class='line' id='LC1819'><span class="sd">    be run with a particular Python version.</span></div><div class='line' id='LC1820'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC1821'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">__file__</span></div><div class='line' id='LC1822'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;.pyc&#39;</span><span class="p">):</span></div><div class='line' id='LC1823'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">filename</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC1824'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="n">codecs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="s">&#39;r&#39;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s">&#39;utf-8&#39;</span><span class="p">)</span></div><div class='line' id='LC1825'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">content</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span></div><div class='line' id='LC1826'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC1827'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">py_exe</span> <span class="o">=</span> <span class="s">&#39;python</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">python_version</span></div><div class='line' id='LC1828'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">content</span> <span class="o">=</span> <span class="p">((</span><span class="s">&#39;#!/usr/bin/env </span><span class="si">%s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">py_exe</span><span class="p">)</span></div><div class='line' id='LC1829'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">+</span> <span class="s">&#39;## WARNING: This file is generated</span><span class="se">\n</span><span class="s">&#39;</span></div><div class='line' id='LC1830'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">+</span> <span class="n">content</span><span class="p">)</span></div><div class='line' id='LC1831'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">content</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;##EXT&#39;</span> <span class="s">&#39;END##&#39;</span><span class="p">,</span> <span class="n">extra_text</span><span class="p">)</span></div><div class='line' id='LC1832'><br/></div><div class='line' id='LC1833'><span class="c">##EXTEND##</span></div><div class='line' id='LC1834'><br/></div><div class='line' id='LC1835'><span class="k">def</span> <span class="nf">convert</span><span class="p">(</span><span class="n">s</span><span class="p">):</span></div><div class='line' id='LC1836'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">b</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64decode</span><span class="p">(</span><span class="n">s</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&#39;ascii&#39;</span><span class="p">))</span></div><div class='line' id='LC1837'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">zlib</span><span class="o">.</span><span class="n">decompress</span><span class="p">(</span><span class="n">b</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s">&#39;utf-8&#39;</span><span class="p">)</span></div><div class='line' id='LC1838'><br/></div><div class='line' id='LC1839'><span class="c">##file site.py</span></div><div class='line' id='LC1840'><span class="n">SITE_PY</span> <span class="o">=</span> <span class="n">convert</span><span class="p">(</span><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC1841'><span class="s">eJzFPf1z2zaWv/OvwMqToZTIdOJ0e3tOnRsncVrvuYm3SWdz63q0lARZrCmSJUjL2pu7v/3eBwAC</span></div><div class='line' id='LC1842'><span class="s">JCXbm+6cphNLJPDw8PC+8PAeOhgMTopCZnOxyud1KoWScTlbiiKulkos8lJUy6Sc7xdxWW3g6ewm</span></div><div class='line' id='LC1843'><span class="s">vpZKVLlQGxVhqygInn7lJ3gqPi8TZVCAb3Fd5au4SmZxmm5EsiryspJzMa/LJLsWSZZUSZwm/4AW</span></div><div class='line' id='LC1844'><span class="s">eRaJp1+PQXCWCZh5mshS3MpSAVwl8oW42FTLPBPDusA5v4j+GL8cjYWalUlRQYNS4wwUWcZVkEk5</span></div><div class='line' id='LC1845'><span class="s">BzShZa2AlEkl91UhZ8kimdmG67xO56JI45kUf/87T42ahmGg8pVcL2UpRQbIAEwJsArEA74mpZjl</span></div><div class='line' id='LC1846'><span class="s">cxkJ8UbOYhyAnzfEChjaGNdMIRmzXKR5dg1zyuRMKhWXGzGc1hUBIpTFPAecEsCgStI0WOfljRrB</span></div><div class='line' id='LC1847'><span class="s">ktJ6rOGRiJk9/Mkwe8A8cfwu5wCOH7Pg5yy5GzNs4B4EVy2ZbUq5SO5EjGDhp7yTs4l+NkwWYp4s</span></div><div class='line' id='LC1848'><span class="s">FkCDrBphk4ARUCJNpgcFLcd3eoVeHxBWlitjGEMiytyYX1KPKDirRJwqYNu6QBopwvydnCZxBtTI</span></div><div class='line' id='LC1849'><span class="s">bmE4gAgkDfrGmSeqsuPQ7EQOAEpcxwqkZKXEcBUnGTDrj/GM0P5rks3ztRoRBWC1lPi1VpU7/2EP</span></div><div class='line' id='LC1850'><span class="s">AaC1Q4BxgItlVrPO0uRGppsRIPAZsC+lqtMKBWKelHJW5WUiFQEA1DZC3gHSYxGXUpOQOdPI7Zjo</span></div><div class='line' id='LC1851'><span class="s">TzRJMlxYFDAUeHyJJFkk13VJEiYWCXAucMX7jz+Jd6dvzk4+aB4zwFhmr1eAM0ChhXZwggHEQa3K</span></div><div class='line' id='LC1852'><span class="s">gzQHgY6Cc/wj4vkchewaxwe8mgYH9650MIS5F1G7j7PgQHa9uHoYmGMFyoTGCqjff0OXsVoCff7n</span></div><div class='line' id='LC1853'><span class="s">nvUOgpNtVKGJ87f1MgeZzOKVFMuY+Qs5I/hOw3kdFdXyFXCDQjgVkErh4iCCCcIDkrg0G+aZFAWw</span></div><div class='line' id='LC1854'><span class="s">WJpkchQAhabU1l9FYIUPebZPa93iBIBQBhm8dJ6NaMRMwkS7sF6hvjCNNzQz3SSw67zKS1IcwP/Z</span></div><div class='line' id='LC1855'><span class="s">jHRRGmc3hKMihuJvU3mdZBkihLwQhHshDaxuEuDEeSTOqRXpBdNIhKy9uCWKRA28hEwHPCnv4lWR</span></div><div class='line' id='LC1856'><span class="s">yjGLL+rW3WqEBpOVMGudMsdBy4rUK61aM9Ve3juMvrS4jtCslqUE4PXUE7pFno/FFHQ2YVPEKxav</span></div><div class='line' id='LC1857'><span class="s">ap0T5wQ98kSdkCeoJfTF70DRE6XqlbQvkVdAsxBDBYs8TfM1kOwoCITYw0bGKPvMCW/hHfwLcPHf</span></div><div class='line' id='LC1858'><span class="s">VFazZRA4I1nAGhQivw0UAgGTIDPN1RoJj9s0K7eVTJKxpsjLuSxpqIcR+4ARf2BjnGvwIa+0UePp</span></div><div class='line' id='LC1859'><span class="s">4irnq6RClTTVJjNhi5eFFevHVzxvmAZYbkU0M00bOq1wemmxjKfSuCRTuUBJ0Iv0yi47jBn0jEm2</span></div><div class='line' id='LC1860'><span class="s">uBIrtjLwDsgiE7Yg/YoFlc6ikuQEAAwWvjhLijqlRgoZTMQw0Kog+KsYTXqunSVgbzbLASokNt8z</span></div><div class='line' id='LC1861'><span class="s">sD+A2z9AjNbLBOgzAwigYVBLwfJNk6pEB6HRR4Fv9E1/Hh849WyhbRMPuYiTVFv5OAvO6OFpWZL4</span></div><div class='line' id='LC1862'><span class="s">zmSBvcaaGApmmFXo2l1nQEcU88FgEATGHdoo8zVXQVVujoAVhBlnMpnWCRq+yQRNvf6hAh5FOAN7</span></div><div class='line' id='LC1863'><span class="s">3Ww7Cw80hOn0AajkdFmU+Qpf27l9AmUCY2GPYE9ckJaR7CB7nPgKyeeq9MI0RdvtsLNAPRRc/HT6</span></div><div class='line' id='LC1864'><span class="s">/uzL6SdxLC4blTZu67MrGPM0i4GtySIAU7WGbXQZtETFl6DuE+/BvBNTgD2j3iS+Mq5q4F1A/XNZ</span></div><div class='line' id='LC1865'><span class="s">02uYxsx7GZx+OHlzfjr5+dPpT5NPZ59PAUGwMzLYoymjeazBYVQRCAdw5VxF2r4GnR704M3JJ/sg</span></div><div class='line' id='LC1866'><span class="s">mCRq8u03wG7wZHgtK2DicggzHotwFd8pYNBwTE1HiGOnAVjwcDQSr8Xh06cvDwlasSk2AAzMrtMU</span></div><div class='line' id='LC1867'><span class="s">H060RZ8k2SIPR9T4V3bpj1lJaf/t8uibK3F8LMJf49s4DMCHapoyS/xI4vR5U0joWsGfYa5GQTCX</span></div><div class='line' id='LC1868'><span class="s">CxC9G4kCOnxKfvGIO8CSQMtc2+lf8yQz75kr3SFIfwypB+AwmczSWClsPJmEQATq0POBDhE71yh1</span></div><div class='line' id='LC1869'><span class="s">Q+hYbNyuI40KfkoJC5thlzH+04NiPKV+iAaj6HYxjUBcV7NYSW5F04d+kwnqrMlkqAcEYSaJAYeL</span></div><div class='line' id='LC1870'><span class="s">1VAoTBPUWWUCfi1xHuqwqcpT/InwUQuQAOLWCrUkLpLeOkW3cVpLNXQmBUQcDltkREWbKOJHcFGG</span></div><div class='line' id='LC1871'><span class="s">YImbpRuN2tQ0PAPNgHxpDlq0bFEOP3vg74C6Mps43Ojx3otphpj+mXcahAO4nCGqe6VaUFg7iovT</span></div><div class='line' id='LC1872'><span class="s">C/Hy+eE+ujOw55xb6njN0UInWS3twwWslpEHRph7GXlx6bJAPYtPj3bDXEV2ZbqssNBLXMpVfivn</span></div><div class='line' id='LC1873'><span class="s">gC0ysLPK4id6AztzmMcshlUEvU7+AKtQ4zfGuA/l2YO0oO8A1FsRFLP+Zun3OBggMwWKiDfWRGq9</span></div><div class='line' id='LC1874'><span class="s">62dTWJT5bYLOxnSjX4KtBGWJFtM4NoGzcB6ToUkEDQFecIaUWssQ1GFZs8NKeCNItBfzRrFGBO4c</span></div><div class='line' id='LC1875'><span class="s">NfUVfb3J8nU24Z3wMSrd4ciyLgqWZl5s0CzBnngPVgiQzGFj1xCNoYDLL1C29gF5mD5MFyhLewsA</span></div><div class='line' id='LC1876'><span class="s">BIZe0XbNgWW2ejRF3jXisAhj9EqQ8JYS/YVbMwRttQwxHEj0NrIPjJZASDA5q+CsatBMhrJmmsHA</span></div><div class='line' id='LC1877'><span class="s">Dkl8rjuPeAvqA2hRMQKzOdTQuJGh3+URKGdx7iolpx9a5C9fvjDbqCXFVxCxKU4aXYgFGcuo2IBh</span></div><div class='line' id='LC1878'><span class="s">TUAnGI+MozXEBmtwbgFMrTRriv1PIi/YG4P1vNCyDX4A7O6qqjg6OFiv15GOLuTl9YFaHPzxT99+</span></div><div class='line' id='LC1879'><span class="s">+6fnrBPnc+IfmI4jLTrUFh3QO/Roo++MBXptVq7Fj0nmcyPBGkryysgVRfy+r5N5Lo72R1Z/Ihc3</span></div><div class='line' id='LC1880'><span class="s">Zhr/Na4MKJCJGZSpDLQdNBg9UftPopdqIJ6QdbZthyP2S7RJtVbMt7rQo8rBEwC/ZZbXaKobTlDi</span></div><div class='line' id='LC1881'><span class="s">GVg32KHP5bS+Du3gno00P2CqKKdDywP7L64QA58zDF8ZUzxBLUFsgRbfIf1PzDYxeUdaQyB50UR1</span></div><div class='line' id='LC1882'><span class="s">ds+bfi1miDt/uLxbX9MRGjPDRCF3oET4TR4sgLZxV3Lwo11btHuOa2s+niEwlj4wzKsdyyEKDuGC</span></div><div class='line' id='LC1883'><span class="s">azF2pc7havR4QZrWrJpBwbiqERQ0OIlTprYGRzYyRJDo3ZjNPi+sbgF0akUOTXzArAK0cMfpWLs2</span></div><div class='line' id='LC1884'><span class="s">KzieEPLAsXhBTyS4yEedd895aes0pYBOi0c9qjBgb6HRTufAl0MDYCwG5c8Dbmm2KR9bi8Jr0AMs</span></div><div class='line' id='LC1885'><span class="s">5xgQMtiiw0z4xvUBB3uDHnbqWP1tvZnGfSBwkYYci3oQdEL5mEcoFUhTMfR7bmNxS9zuYDstDjGV</span></div><div class='line' id='LC1886'><span class="s">WSYSabVFuNrKo1eodhqmRZKh7nUWKZqlOXjFVisSIzXvfWeB9kH4uM+YaQnUZGjI4TQ6Jm/PE8BQ</span></div><div class='line' id='LC1887'><span class="s">t8Pw2XWNgQY3DoMYrRJF1g3JtIR/wK2g+AYFo4CWBM2CeaiU+RP7HWTOzld/2cIeltDIEG7TbW5I</span></div><div class='line' id='LC1888'><span class="s">x2JoOOb9nkAy6mgMSEEGJOwKI7mOrA5S4DBngTzhhtdyq3QTjEiBnDkWhNQM4E4vvQ0OPonwBIQk</span></div><div class='line' id='LC1889'><span class="s">FCHfVUoW4pkYwPK1RfVhuvt35VIThBg6DchV0NGLYzey4UQ1jltRDp+h/fgGnZUUOXDwFFweN9Dv</span></div><div class='line' id='LC1890'><span class="s">srlhWht0AWfdV9wWKdDIFIcZjFxUrwxh3GDyH46dFg2xzCCGobyBvCMdM9IosMutQcOCGzDemrfH</span></div><div class='line' id='LC1891'><span class="s">0o/diAX2HYa5OpSrO9j/hWWiZrkKKWbSjl24H80VXdpYbM+T6QD+eAswGF15kGSq4xcYZfknBgk9</span></div><div class='line' id='LC1892'><span class="s">6GEfdG+yGBaZx+U6yUJSYJp+x/7SdPCwpPSM3MEn2k4dwEQx4nnwvgQBoaPPAxAn1ASwK5eh0m5/</span></div><div class='line' id='LC1893'><span class="s">F+zOKQ4sXO4+8Nzmy6OXV13ijrdFeOynf6lO76oyVrhaKS8aCwWuVteAo9KFycXZRh9e6sNt3CaU</span></div><div class='line' id='LC1894'><span class="s">uYJdpPj46YtAQnBcdx1vHjf1huERm3vn5H0M6qDX7iVXa3bELoAIakVklIPw8Rz5cGQfO7kdE3sE</span></div><div class='line' id='LC1895'><span class="s">kEcxzI5FMZA0n/wzcHYtFIyxP99kGEdrqwz8wOtvv5n0REZdJL/9ZnDPKC1i9In9sOUJ2pE5qWDX</span></div><div class='line' id='LC1896'><span class="s">bEsZp+RqOH0oqJg1rGPbFCPW57T90zx21eNzarRs7Lu/BX4MFAypS/ARno8bsnWnih/fndoKT9up</span></div><div class='line' id='LC1897'><span class="s">HcA6u1Xz2aNFgL19Pv0VdshKB9Vu4ySlcwWY/P4+Klezued4Rb/28CDtVDAOCfr2X+ryOXBDyNGE</span></div><div class='line' id='LC1898'><span class="s">UXc62hk7MQHnnl2w+RSx6qKyp3MImiMwLy/APf7sQtUWzDDucz5eOOxRTd6M+5yJr1Gr+PldNJAF</span></div><div class='line' id='LC1899'><span class="s">5tFg0Ef2rez4/zHL5/+aST5wKubk+ne0ho8E9HvNhI0HQ9PGw4fVv+yu3TXAHmCetridO9zC7tB8</span></div><div class='line' id='LC1900'><span class="s">Vrkwzh2rJCWeou56KtaUrkCxVTwpAihz9vt64OAy6kPvt3VZ8tE1qcBClvt4HDsWmKllPL9eE7Mn</span></div><div class='line' id='LC1901'><span class="s">Dj7ICjGxzWYUq3byevI+NRLq6LOdSdjsG/rlbJmbmJXMbpMS+oLCHYY/fPzxNOw3IRjHhU4PtyIP</span></div><div class='line' id='LC1902'><span class="s">9xsQ7iOYNtTECR/Thyn0mC7/vFS1ty4+QU1GgIkIa7L12gc/EGziCP1rcE9EyDuw5WN23KHPlnJ2</span></div><div class='line' id='LC1903'><span class="s">M5GUOoBsil2doPhbfI2Y2IwCP/9LxQtKYoOZzNIaacWON2YfLupsRucjlQT/SqcKY+oQJQRw+G+R</span></div><div class='line' id='LC1904'><span class="s">xtdiSJ3nGHrS3EjRqdu41N5nUeaYnCrqZH5wncyF/K2OU9zWy8UCcMHDK/0q4uEpAiXecU4DJy0q</span></div><div class='line' id='LC1905'><span class="s">OavLpNoACWKV67M/Sn9wGk43PNGhhyQf8zABMSHiSHzCaeN7JtzckMsEB/wTD5wk7ruxg5OsENFz</span></div><div class='line' id='LC1906'><span class="s">eJ/lExx1Qjm+Y0aqey5Pj4P2CDkAGABQmP9gpCN3/htJr9wDRlpzl6ioJT1SupGGnJwxhDIcYaSD</span></div><div class='line' id='LC1907'><span class="s">f9NPnxFd3tqC5fV2LK93Y3ndxvK6F8trH8vr3Vi6IoELa4NWRhL6AlftY43efBs35sTDnMazJbfD</span></div><div class='line' id='LC1908'><span class="s">3E/M8QSIojAbbCNTnALtRbb4fI+AkNp2DpzpYZM/k3BSaZlzCFyDRO7HQyy9mTfJ605nysbRnXkq</span></div><div class='line' id='LC1909'><span class="s">xp3dlkPk9z2IIkoVm1J3lrd5XMWRJxfXaT4FsbXojhsAY9FOJ+JYaXY7mXJ0t2WpBhf/9fmHjx+w</span></div><div class='line' id='LC1910'><span class="s">OYIamPQG6oaLiIYFpzJ8GpfXqitNzeavAHakln4iDnXTAPceGFnjUfb4n3eU4YGMI9aUoZCLAjwA</span></div><div class='line' id='LC1911'><span class="s">yuqyzdzcpzBsPddJUvo5MzkfNh2LQVYNmkltIdLJxcW7k88nAwr5Df534AqMoa0vHS4+poVt0PXf</span></div><div class='line' id='LC1912'><span class="s">3OaW4tgHhFrHthrj587Jo3XDEffbWAO248O3Hhw+xGD3hgn8Wf5LKQVLAoSKdPD3MYR68B7oq7YJ</span></div><div class='line' id='LC1913'><span class="s">HfoYRuwk/7kna+ys2HeO7DkuiiP6fccO7QH8w07cY0yAANqFGpqdQbOZail9a153UNQB+kBf76u3</span></div><div class='line' id='LC1914'><span class="s">YO2tV3sn41PUTqLHAXQoa5ttd/+8cxo2ekpWb06/P/twfvbm4uTzD44LiK7cx08Hh+L0xy+C8kPQ</span></div><div class='line' id='LC1915'><span class="s">gLFPFGNqRIWZSGBY3EInMc/hvxojP/O64iAx9Hp3fq5PalZY6oK5z2hzInjOaUwWGgfNOAptH+r8</span></div><div class='line' id='LC1916'><span class="s">I8Qo1Rskp6aI0nWo5gj3SyuuZ1G5zo+mUqUpOqu13nrpWjFTU0bn2hFIHzR2ScEgOMUMXlEWe2V2</span></div><div class='line' id='LC1917'><span class="s">hSWfAOo6qx6ktI22iSEpBQU76QLO+Zc5XfECpdQZnjSdtaK/DF1cw6tIFWkCO7lXoZUl3Q3TYxrG</span></div><div class='line' id='LC1918'><span class="s">0Q/tATfj1acBne4wsm7Is96KBVqtVyHPTfcfNYz2Ww0YNgz2DuadSUoPoQxsTG4TITbik5xQ3sFX</span></div><div class='line' id='LC1919'><span class="s">u/R6DRQsGB70VbiIhukSmH0Mm2uxTGADATy5BOuL+wSA0FoJ/0DgyIkOyByzM8K3q/n+X0JNEL/1</span></div><div class='line' id='LC1920'><span class="s">L7/0NK/KdP9vooBdkOBUorCHmG7jd7DxiWQkTj++H4WMHKXmir/UWB4ADgkFQB1pp/wlPkGfDJVM</span></div><div class='line' id='LC1921'><span class="s">Fzq/xNcH+EL7CfS61b2URam797vGIUrAEzUkr+GJMvQLMd3Lwh7jVEYt0Fj5YDHDCkI3DcF89sSn</span></div><div class='line' id='LC1922'><span class="s">pUxTne9+9u78FHxHLMZACeJzt1MYjuMleISuk++4wrEFCg/Y4XWJbFyiC0tJFvPIa9YbtEaRo95e</span></div><div class='line' id='LC1923'><span class="s">XoZdJwoMd3t1osBlnCgX7SFOm2GZcoIIWRnWwiwrs3arDVLYbUMUR5lhlphclJTA6vME8DI9jXlL</span></div><div class='line' id='LC1924'><span class="s">BHslLPUwEXg+RU6yymQspskM9CioXFCoYxASJC7WMxLn5RnHwPNSmTIoeFhsyuR6WeHpBnSOqAQD</span></div><div class='line' id='LC1925'><span class="s">m/948uX87AOVJRy+bLzuHuYc005gzEkkx5giiNEO+OKm/SFXTSZ9PKtfIQzUPvCn/YqzU455gE4/</span></div><div class='line' id='LC1926'><span class="s">Dizin/YrrkM7dnaCPANQUHXRFg/cADjd+uSmkQXG1e6D8eOmADaY+WAoFollLzrRw51flxNty5Yp</span></div><div class='line' id='LC1927'><span class="s">obiPefmIA5xFYVPSdGc3Ja390XNcFHjONR/2N4K3fbJlPlPoetN5sy35zf10pBBLYgGjbmt/DJMd</span></div><div class='line' id='LC1928'><span class="s">1mmqp+Mw2zZuoW2ttrG/ZE6s1Gk3y1CUgYhDt/PIZbJ+JaybMwd6adQdYOI7ja6RxF5VPvglG2gP</span></div><div class='line' id='LC1929'><span class="s">w8PEEruzTzEdqYyFjABGMqSu/anBh0KLAAqEsn+HjuSOR08PvTk61uD+OWrdBbbxB1CEOheXajzy</span></div><div class='line' id='LC1930'><span class="s">EjgRvvzGjiO/IrRQjx6J0PFUMpnlNk8MP+slepUv/Dn2ygAFMVHsyji7lkOGNTYwn/nE3hKCJW3r</span></div><div class='line' id='LC1931'><span class="s">kfoyueozLOIMnNO7LRzelYv+gxODWosROu1u5KatjnzyYIPeUpCdBPPBl/EadH9RV0NeyS3n0L21</span></div><div class='line' id='LC1932'><span class="s">dNuh3g8Rsw+hqT59H4YYjvkt3LI+DeBeamhY6OH9tuUUltfGOLLWPraqmkL7QnuwsxK2ZpWiYxmn</span></div><div class='line' id='LC1933'><span class="s">ONH4otYLaAzucWPyB/apThSyv3vqxJyYkAXKg7sgvbkNdINWOGHA5UpcOZpQOnxTTaPfzeWtTMFo</span></div><div class='line' id='LC1934'><span class="s">gJEdYrXDr7baYRTZcEpvHthXY3exudj040ZvGsyOTDkGIkCFGL2Bnl0INTjgCv+idyJxdkPO8du/</span></div><div class='line' id='LC1935'><span class="s">no3F2w8/wb9v5EewoFjzOBZ/g9HF27yEbSUX7dJtCljAUfF+Ma8VFkYSNDqh4Isn0Fu78MiLpyG6</span></div><div class='line' id='LC1936'><span class="s">ssQvKbEKUmAybbni204ARZ4gFbI37oGpl4DfpqCr5YQaB7FvLQb6JdJge40L1oUc6JbRslqlaCac</span></div><div class='line' id='LC1937'><span class="s">4EiziJeD87O3px8+nUbVHTK2+Tlwgid+HhZORx8Nl3gMNhb2yazGJ1eOv/yDTIsed1nvNU29DO41</span></div><div class='line' id='LC1938'><span class="s">RQjbkcLuL/kmjdjuKeISAwai2MzzWYQtgdO5RK9ag/88craV99p3z7girOFIH541Tjw+BmqIX9r6</span></div><div class='line' id='LC1939'><span class="s">ZwANqY+eE/UkhOIp1orx42jQb4HHgiLa8OfpzXruBsR10Q9NsI1pM+uh392qwCXTWcOznER4Hdtl</span></div><div class='line' id='LC1940'><span class="s">MHWgaRKr1XTm1gd+zIS+CAWUGx1vyEVcp5WQGWylaG9PN1KAgndL+lhCmFXYilGdG0Vn0nW8UU7u</span></div><div class='line' id='LC1941'><span class="s">UazEAEcdUFE9nsNQoBC23j/GN2wGsNZQ1FwCDdAJUdo25U5XVc+WLMG8EyLq9eQbrJPspZvGoynM</span></div><div class='line' id='LC1942'><span class="s">g/LGeNb4rzBP9BYZo2tZ6fnzg+Ho8kWT4EDB6JlX0DsrwNi5bLIHGrN4+vTpQPzH/U4PoxKleX4D</span></div><div class='line' id='LC1943'><span class="s">3hjA7nVWzun1FoOtJ2dXq+vQmzcR8ONsKS/hwRUFze3zOqOI5I6utCDS/jUwQlyb0DKjad8yxxyr</span></div><div class='line' id='LC1944'><span class="s">K/l8mVvwOZU2GD9nCV13hBElicpW3xqF0SYjTcSSoBjCWM2SJOToBKzHJq+xFg+ji5pf5B1wfIJg</span></div><div class='line' id='LC1945'><span class="s">xvgWD8Z4h71Ex5LyZi33WHSOxYAADyiljEejYmaqRgM8JxcbjebkLEuqpozkuXtmqq8AqOwtRpqv</span></div><div class='line' id='LC1946'><span class="s">RLxGyTDzaBHDKev0WLVxrPOdLOptVPLZpRtnbM2SX9+HO7A2SFq+WBhM4aFZpFkuy5kxp7hiySyp</span></div><div class='line' id='LC1947'><span class="s">HDCmHcLhznR5E1mfKOhBaQDqnazC3Eq0ffsHuy4uph/p+HjfjKSzhip7IRbHhOKslVcYRc34FH2y</span></div><div class='line' id='LC1948'><span class="s">hLR8a76MYJQPFM3WnoA3lviDjqViDYF3b4dbzlhn+j4OTttoLukAOHQHlFWQlh09HeFcPGbhM9Nu</span></div><div class='line' id='LC1949'><span class="s">uUUDP7QzJ9xuk7Kq43Sir32YoJ82sefpGk9bBrezwNN6K+Db5+D47uuMfXAcTHIN0hMzbk1FxrFY</span></div><div class='line' id='LC1950'><span class="s">6MhE5FaW+UVYRY5e3iH7SuBTIGXmE1MPbWJHl5ZdbaGpTtV0VDyCemaKl7Y45KZqplNw4mI+pvQm</span></div><div class='line' id='LC1951'><span class="s">U+6wxXn2M0fp6grxWgxfjsVha+czKzZ4kxMg+2Qe+q4YdYOpOMEAM8f2vRji9bEYvhiLP+6AHm0Z</span></div><div class='line' id='LC1952'><span class="s">4OjQHaG9j21B2Ark5dWjyZgmUyJb2JfCfn9fncMImp5xHF21yd8l03dEpX9vUYkrBHWi8ot2onJr</span></div><div class='line' id='LC1953'><span class="s">7K371s7HRzJcgeJYJHK+/0QhCTXSjW7ezuCEHxbQ79kcLV073lTUUOHcFDYj60YPOhrRuM12EFOU</span></div><div class='line' id='LC1954'><span class="s">rtUX1++irmHDae8cMGkyrVRFe8scpjFq9FpEBQCTvqM0/IZ3u8B7TQrXP9t6xKqLACzYngiCrvTk</span></div><div class='line' id='LC1955'><span class="s">A7OmYSOo9zqCj9IA9zCKCPEwtVEUrmQ9QkRCugeHmOhZ6xDb4fjfnXm4xGDbUWgHy2+/2YWnK5i9</span></div><div class='line' id='LC1956'><span class="s">RR09C7q70sITWVte0Sy3+fQH5jxG6ev6VQLjQGlEB5xVc1UluZlHmL3Md9DkNot5hZdB0sk0msRU</span></div><div class='line' id='LC1957'><span class="s">um4Tb6X51i/0Yyh2QMlksBbgSdULPEi+pbstTxQlveEVNd8cvhibymAGpCfwMnr5TF8BSd3M5Qe+</span></div><div class='line' id='LC1958'><span class="s">jz3Wezd4qfsdRv/mAEsqv7d91dnN0LSOW3dB+YOFFD0bRRNLh8Yw3V8H0qxZLPDOxIaY7FvbC0De</span></div><div class='line' id='LC1959'><span class="s">g7czBT/HXH6ag8MGG9KoD11XYzTSu021bRHg+03GNsl5UNdGkSLSu4Rtm/LcpTgfLQq6V78FwRAC</span></div><div class='line' id='LC1960'><span class="s">cv4y5jfoCtbFkQ2xGZuCJ59DN5sTP9VNb90Z2xM0ttVNuGv63H/X3HWLwM7cJDN05u7Xl7o00H23</span></div><div class='line' id='LC1961'><span class="s">W9E+GnB4QxPiQSUSjcbvNyauHRjrHJr+CL3+IPndTjjTLWblPjAmYwfj/cSeGntj9lfxzP2OCWH7</span></div><div class='line' id='LC1962'><span class="s">fCGzW07c62y0pt2xGW2Of4inwMkv+NzeMEAZTXPNgbxfohv2JpwjO5HX12oS4+2OE9pkUz5XZ/dk</span></div><div class='line' id='LC1963'><span class="s">tm3v6XI+GauN2W3hpUUAwnCTzrx1k+uBMUBX8i3TnA7l3E4jaGhKGnaykFUyZ5Ogt3YALuKIKfU3</span></div><div class='line' id='LC1964'><span class="s">gXhOIx6kEgPdqi6LEnbDA30XMefp9KU2N0BNAG8VqxuDuukx1lfTkmKl5DBTgsxx2laSDxCBjXjH</span></div><div class='line' id='LC1965'><span class="s">NEwm9h3wyvPmmoVkbJlBZvVKlnHVXDHkZwQksOlqRqCic1xcJzzXSGWLS1zEEssbDlIYILPfn8HG</span></div><div class='line' id='LC1966'><span class="s">0ttU77hXYWS13cPZiXrokO9jrmxwjJHh4uTOXi/oXms1p6utXe/QNmu4zl6pBMtg7sojHaljZfxW</span></div><div class='line' id='LC1967'><span class="s">39/Fd8xyJB/9S4d/QN7dyks/C92qM/ZuLRrOM1chdC9swhsDyDj33cPY4YDujYutDbAd39cXllE6</span></div><div class='line' id='LC1968'><span class="s">HuaWxpaK2ifvVTjNaKMmgoQJo/dEkPyigEdGkDz4D4wg6VszwdBofLQe6C0TuCfUxOrBvYKyYQTo</span></div><div class='line' id='LC1969'><span class="s">MwEi4QF26wJDYyqHbtJ9kavkbmAvlGZd6VTyGfOAHNm9m4xA8FWTys1Q9q6C2xVB8qWLHn9//vHN</span></div><div class='line' id='LC1970'><span class="s">yTnRYnJx8vY/T76npCw8LmnZqgeH2LJ8n6m976V/u+E2nUjTN3iDbc8NsVzDpCF03ndyEHog9Ner</span></div><div class='line' id='LC1971'><span class="s">9S1oW5G5r7d16NT9dDsB4run3YK6TWX3Qu74ZbrGxE2faeVpB/opJ9WaX05mgnlkTupYHJqTOPO+</span></div><div class='line' id='LC1972'><span class="s">OTzRMtqJLW9bOCe9tatOtL+qbwHdEvce2SRrWgE8M0H+skcmpmLGBubZQWn/bz4oMxyrDc0NOiCF</span></div><div class='line' id='LC1973'><span class="s">M+nc5EiXODKoyv//iZSg7GLc27GjOLZ3c1M7Ph5S9tJ5PPudycgQxCv3G3Tn5wr7XKZbqBAErPD0</span></div><div class='line' id='LC1974'><span class="s">PYWMiNF/+kDVph88UeJynwqL91HZXNlfuGbauf1rgkkGlb3vS3GCEh+zQuNFnbqJA7ZPpwM5fXQa</span></div><div class='line' id='LC1975'><span class="s">lS+cShbQfAdA50Y8FbA3+kusEKcbEcLGUbtkmBxLdNSX9TnIo910sDe0ei72t5WdumWXQrzY3nDe</span></div><div class='line' id='LC1976'><span class="s">quzUPQ65h7qnh6pNcZ9jgTFLc1s9qXhNkPk4U9AFX57zgWfoetsPX28vXxzZwwXkd3ztKBLKJhs4</span></div><div class='line' id='LC1977'><span class="s">hv3Sycbceamk052YpRxTuh7u1ZyQsG5x5UBln2Db3qZTkrJl/2PyHBjSwHvfHzIzPbyr9wdtTC3r</span></div><div class='line' id='LC1978'><span class="s">HcGUxPCJGtG0nCIejbt9MupOt1FbXSBckPQAIB0VCLAQTEc3OgmiG87yHj7Xu8FpTdfxuidMoSMV</span></div><div class='line' id='LC1979'><span class="s">lCzmcwT3ML5fg1+7OxUSP6g7o2j6c4M2B+olB+Fm34FbjbxQyHaT0J56wwdbXACuye7v/+IB/btp</span></div><div class='line' id='LC1980'><span class="s">jLb74S6/2rZ62VsHyL4sZr5iZlCLROZxBEYG9OaQtDWWSxhBx2toGjq6DNXMDfkCHT/KpsXLtmmD</span></div><div class='line' id='LC1981'><span class="s">Qc7sRHsA1igE/wfVIOdx</span></div><div class='line' id='LC1982'><span class="s">&quot;&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC1983'><br/></div><div class='line' id='LC1984'><span class="c">##file activate.sh</span></div><div class='line' id='LC1985'><span class="n">ACTIVATE_SH</span> <span class="o">=</span> <span class="n">convert</span><span class="p">(</span><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC1986'><span class="s">eJytVVFvokAQfudXTLEPtTlLeo9tvMSmJpq02hSvl7u2wRUG2QR2DSxSe7n/frOACEVNLlceRHa+</span></div><div class='line' id='LC1987'><span class="s">nfl25pvZDswCnoDPQ4QoTRQsENIEPci4CsBMZBq7CAsuLOYqvmYKTTj3YxnBgiXBudGBjUzBZUJI</span></div><div class='line' id='LC1988'><span class="s">BXEqgCvweIyuCjeG4eF2F5x14bcB9KQiQQWrjSddI1/oQIx6SYYeoFjzWIoIhYI1izlbhJjkKO7D</span></div><div class='line' id='LC1989'><span class="s">M/QEmKfO9O7WeRo/zr4P7pyHwWxkwitcgwpQ5Ej96OX+PmiFwLeVjFUOrNYKaq1Nud3nR2n8nI2m</span></div><div class='line' id='LC1990'><span class="s">k9H0friPTGVsUdptaxGrTEfpNVFEskxpXtUkkCkl1UNF9cgLBkx48J4EXyALuBtAwNYIjF5kcmUU</span></div><div class='line' id='LC1991'><span class="s">abMKmMq1ULoiRbgsDEkTSsKSGFCJ6Z8vY/2xYiSacmtyAfCDdCNTVZoVF8vSTQOoEwSnOrngBkws</span></div><div class='line' id='LC1992'><span class="s">MYGMBMg8/bMBLSYKS7pYEXP0PqT+ZmBT0Xuy+Pplj5yn4aM9nk72JD8/Wi+Gr98sD9eWSMOwkapD</span></div><div class='line' id='LC1993'><span class="s">BbUv91XSvmyVkICt2tmXR4tWmrcUCsjWOpw87YidEC8i0gdTSOFhouJUNxR+4NYBG0MftoCTD9F7</span></div><div class='line' id='LC1994'><span class="s">2rTtxG3oPwY1b2HncYwhrlmj6Wq924xtGDWqfdNxap+OYxplEurnMVo9RWks+rH8qKEtx7kZT5zJ</span></div><div class='line' id='LC1995'><span class="s">4H7oOFclrN6uFe+d+nW2aIUsSgs/42EIPuOhXq+jEo3S6tX6w2ilNkDnIpHCWdEQhFgwj9pkk7FN</span></div><div class='line' id='LC1996'><span class="s">l/y5eQvRSIQ5+TrL05lewxWpt/Lbhes5cJF3mLET1MGhcKCF+40tNWnUulxrpojwDo2sObdje3Bz</span></div><div class='line' id='LC1997'><span class="s">N3QeHqf3D7OjEXMVV8LN3ZlvuzoWHqiUcNKHtwNd0IbvPGKYYM31nPKCgkUILw3KL+Y8l7aO1ArS</span></div><div class='line' id='LC1998'><span class="s">Ad37nIU0fCj5NE5gQCuC5sOSu+UdI2NeXg/lFkQIlFpdWVaWZRfvqGiirC9o6liJ9FXGYrSY9mI1</span></div><div class='line' id='LC1999'><span class="s">D/Ncozgn13vJvsznr7DnkJWXsyMH7e42ljdJ+aqNDF1bFnKWFLdj31xtaJYK6EXFgqmV/ymD/ROG</span></div><div class='line' id='LC2000'><span class="s">+n8O9H8f5vsGOWXsL1+1k3g=</span></div><div class='line' id='LC2001'><span class="s">&quot;&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC2002'><br/></div><div class='line' id='LC2003'><span class="c">##file activate.fish</span></div><div class='line' id='LC2004'><span class="n">ACTIVATE_FISH</span> <span class="o">=</span> <span class="n">convert</span><span class="p">(</span><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC2005'><span class="s">eJydVW2P2jgQ/s6vmAZQoVpA9/WkqqJaTou0u6x2uZVOVWWZZEKsS+yc7UDpr+84bziQbauLxEvs</span></div><div class='line' id='LC2006'><span class="s">eXnsZ56ZIWwTYSAWKUJWGAs7hMJgBEdhEwiMKnSIsBNywUMrDtziPBYmCeBDrFUG7v8HmCTW5n8u</span></div><div class='line' id='LC2007'><span class="s">Fu7NJJim81Bl08EQTqqAkEupLOhCgrAQCY2hTU+DQVxIiqgkRNiEBphFEKy+kd1BaFvwFOUBuIxA</span></div><div class='line' id='LC2008'><span class="s">oy20BKtAKp3xFMo0QNtCK5mhtMEA6BmSpUELKo38TThwLfguRVNaiRgs0llnEoIR29zfstf18/bv</span></div><div class='line' id='LC2009'><span class="s">5T17Wm7vAiiN3ONCzfbfwC3DtWXXDqHfAGX0q6z/bO82j3ebh1VwnbrduwTQbvwcRtesAfMGor/W</span></div><div class='line' id='LC2010'><span class="s">L3fs6Xnz8LRlm9fV8/P61sM0LDNwCZjl9gSpCokJRzpryGQ5t8kNGFUt51QjOZGu0Mj35FlYlXEr</span></div><div class='line' id='LC2011'><span class="s">yC09EVOp4lEXfF84Lz1qbhBsgl59vDedXI3rTV03xipduSgt9kLytI3XmBp3aV6MPoMQGNUU62T6</span></div><div class='line' id='LC2012'><span class="s">uQdeefTy1Hfj10zVHg2pq8fXDoHBiOv94csfXwN49xECqWREy7pwukKfvxdMY2j23vXDPuuxxeE+</span></div><div class='line' id='LC2013'><span class="s">JOdCOhxCE3N44B1ZeSLuZh8Mmkr2wEPAmPfKWHA2uxIRjEopdbQYjDz3BWOf14/scfmwoki1eQvX</span></div><div class='line' id='LC2014'><span class="s">ExBdF60Mqh+Y/QcX4uiH4Amwzx79KOVFtbL63sXJbtcvy8/3q5rupmO5CnE91wBviQAhjUUegYpL</span></div><div class='line' id='LC2015'><span class="s">vVEbpLt2/W+PklRgq5Ku6mp+rpMhhCo/lXthQTxJ2ysO4Ka0ad97S7VT/n6YXus6fzk3fLnBZW5C</span></div><div class='line' id='LC2016'><span class="s">KDC6gSO62QDqgFqLCCtPmjegjnLeAdArtSE8VYGbAJ/aLb+vnQutFhk768E9uRbSxhCMzdgEveYw</span></div><div class='line' id='LC2017'><span class="s">IZ5ZqFKl6+kz7UR4U+buqQZXu9SIujrAfD7f0FXpozB4Q0gwp31H9mVTZGGC4b871/wm7lvyDLu1</span></div><div class='line' id='LC2018'><span class="s">FUyvTj/yvD66k3UPTs08x1AQQaGziOl0S1qRkPG9COtBTSTWM9NzQ4R64B+Px/l3tDzCgxv5C6Ni</span></div><div class='line' id='LC2019'><span class="s">e+QaF9xFWrxx0V/G5uvYQOdiZzvYpQUVQSIsTr1TTghI33GnPbTA7/GCqcE3oE3GZurq4HeQXQD6</span></div><div class='line' id='LC2020'><span class="s">32XS1ITj/qLjN72ob0hc5C9bzw8MhfmL</span></div><div class='line' id='LC2021'><span class="s">&quot;&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC2022'><br/></div><div class='line' id='LC2023'><span class="c">##file activate.csh</span></div><div class='line' id='LC2024'><span class="n">ACTIVATE_CSH</span> <span class="o">=</span> <span class="n">convert</span><span class="p">(</span><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC2025'><span class="s">eJx9VG1P2zAQ/u5fcYQKNgTNPtN1WxlIQ4KCUEGaxuQ6yYVYSuzKdhqVX7+zk3bpy5YPUXL3PPfc</span></div><div class='line' id='LC2026'><span class="s">ne98DLNCWshliVDV1kGCUFvMoJGugMjq2qQIiVSxSJ1cCofD1BYRnOVGV0CfZ0N2DD91DalQSjsw</span></div><div class='line' id='LC2027'><span class="s">tQLpIJMGU1euvPe7QeJlkKzgWixlhnAt4aoUVsLnLBiy5NtbJWQ5THX1ZciYKKWwkOFaE04dUm6D</span></div><div class='line' id='LC2028'><span class="s">r/zh7pq/3D7Nnid3/HEy+wFHY/gEJydg0aFaQrBFgz1c5DG1IhTs+UZgsBC2GMFBlaeH+8dZXwcW</span></div><div class='line' id='LC2029'><span class="s">VPvCjXdlAvCfQsE7al0+07XjZvrSCUevR5dnkVeKlFYZmUztG4BdzL2u9KyLVabTU0bdfg7a0hgs</span></div><div class='line' id='LC2030'><span class="s">cSmUg6UwUiQl2iHrcbcVGNvPCiLOe7+cRwG13z9qRGgx2z6DHjfm/Op2yqeT+xvOLzs0PTKHDz2V</span></div><div class='line' id='LC2031'><span class="s">tkckFHoQfQRXoGJAj9el0FyJCmEMhzgMS4sB7KPOE2ExoLcSieYwDvR+cP8cg11gKkVJc2wRcm1g</span></div><div class='line' id='LC2032'><span class="s">QhYFlXiTaTfO2ki0fQoiFM4tLuO4aZrhOzqR4dIPcWx17hphMBY+Srwh7RTyN83XOWkcSPh1Pg/k</span></div><div class='line' id='LC2033'><span class="s">TXX/jbJTbMtUmcxZ+/bbqOsy82suFQg/BhdSOTRhMNBHlUarCpU7JzBhmkKmRejKOQzayQe6MWoa</span></div><div class='line' id='LC2034'><span class="s">n1wqWmuh6LZAaHxcdeqIlVLhIBJdO9/kbl0It2oEXQj+eGjJOuvOIR/YGRqvFhttUB2XTvLXYN2H</span></div><div class='line' id='LC2035'><span class="s">37CBdbW2W7j2r2+VsCn0doVWcFG1/4y1VwBjfwAyoZhD</span></div><div class='line' id='LC2036'><span class="s">&quot;&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC2037'><br/></div><div class='line' id='LC2038'><span class="c">##file activate.bat</span></div><div class='line' id='LC2039'><span class="n">ACTIVATE_BAT</span> <span class="o">=</span> <span class="n">convert</span><span class="p">(</span><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC2040'><span class="s">eJx9UdEKgjAUfW6wfxjiIH+hEDKUFHSKLCMI7kNOEkIf9P9pTJ3OLJ/03HPPPed4Es9XS9qqwqgT</span></div><div class='line' id='LC2041'><span class="s">PbGKKOdXL4aAFS7A4gvAwgijuiKlqOpGlATS2NeMLE+TjJM9RkQ+SmqAXLrBo1LLIeLdiWlD6jZt</span></div><div class='line' id='LC2042'><span class="s">r7VNubWkndkXaxg5GO3UaOOKS6drO3luDDiO5my3iA0YAKGzPRV1ack8cOdhysI0CYzIPzjSiH5X</span></div><div class='line' id='LC2043'><span class="s">0QcvC8Lfaj0emsVKYF2rhL5L3fCkVjV76kShi59NHwDniAHzkgDgqBcwOgTMx+gDQQqXCw==</span></div><div class='line' id='LC2044'><span class="s">&quot;&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC2045'><br/></div><div class='line' id='LC2046'><span class="c">##file deactivate.bat</span></div><div class='line' id='LC2047'><span class="n">DEACTIVATE_BAT</span> <span class="o">=</span> <span class="n">convert</span><span class="p">(</span><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC2048'><span class="s">eJxzSE3OyFfIT0vj4ipOLVEI8wwKCXX0iXf1C7Pl4spMU0hJTcvMS01RiPf3cYmHyQYE+fsGhCho</span></div><div class='line' id='LC2049'><span class="s">cCkAAUibEkTEVhWLMlUlLk6QGixStlyaeCyJDPHw9/Pw93VFsQguim4ZXAJoIUw5DhX47XUM8UCx</span></div><div class='line' id='LC2050'><span class="s">EchHtwsohN1bILUgw61c/Vy4AJYPYm4=</span></div><div class='line' id='LC2051'><span class="s">&quot;&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC2052'><br/></div><div class='line' id='LC2053'><span class="c">##file activate.ps1</span></div><div class='line' id='LC2054'><span class="n">ACTIVATE_PS</span> <span class="o">=</span> <span class="n">convert</span><span class="p">(</span><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC2055'><span class="s">eJylWdmS40Z2fVeE/oHT6rCloNUEAXDThB6wAyQAEjsB29GBjdgXYiWgmC/zgz/Jv+AEWNVd3S2N</span></div><div class='line' id='LC2056'><span class="s">xuOKYEUxM+/Jmzfvcm7W//zXf/+wUMOoXtyi1F9kbd0sHH/hFc2iLtrK9b3FrSqyxaVQwr8uhqJd</span></div><div class='line' id='LC2057'><span class="s">uHaeg9mqzRdR8/13Pyy8qPLdJh0+LMhi0QCoXxYfFh9WtttEnd34H8p6/f1300KauwrULws39e18</span></div><div class='line' id='LC2058'><span class="s">0ZaLNm9rgN/ZVf3h++/e124Vlc0vKsspHy+Yyi5+XbzPhijvCtduoiL/kA1ukWV27n0o7Sb8LIFj</span></div><div class='line' id='LC2059'><span class="s">CvWR5GQgUJdp1Pw8TS9+rPy6SDv/+e3d+0+4qw8f3v20+PliV37efEYBAB9FTKC+RHn/Cfxn3rdv</span></div><div class='line' id='LC2060'><span class="s">00Fube5O+iyCtHDs9BfPfz3q4sfFv9d91Ljhfy7ei0VO+nVTtdOkv/jpt0l2AX6iG1jXgKnnDuD4</span></div><div class='line' id='LC2061'><span class="s">ke2k/i8fzzz5UedkVcP4pwF+Wvz2FJl+3vt598urXf5Y6LNA5WcFOP7r0sW7b9a+W/xcu0Xpv5zk</span></div><div class='line' id='LC2062'><span class="s">Kfq3P9Dz9di/fCxS72MXVU1rpx9L4Bxl85Wmn5a+zP76Zuh3pL9ROWr87PN+//GHIl+oOtvn9XSU</span></div><div class='line' id='LC2063'><span class="s">qH+p0gQBFnx1uV+JLH5O5zv+PXW+WepXVVHZT0+oQezkIATcIm+ivPV/z5J/+cYj3ir4w0Lx09vC</span></div><div class='line' id='LC2064'><span class="s">e5n/y5/Y5LPPfdrqb88ga/PabxZRVfmp39l588m/6u+/e+OpP+dF7n1WZpJ9//Z4v372fDDz9eHB</span></div><div class='line' id='LC2065'><span class="s">7Juvs/BLMHzrxL9+9twXpJfhd1/DrpQ5Euu/vlss3wp9HXC/54C/Ld69m6zwdx3tC0d8daSv0V8B</span></div><div class='line' id='LC2066'><span class="s">n4b9YYF53sJelJV/ix6LZspw/sJtqyl5LJ5r/23htA1Imfm/gt9R7dqVB1LjhydAX4Gb+zksQF59</span></div><div class='line' id='LC2067'><span class="s">9+P7H//U+376afFuvh2/T6P85Xr/5c8C6OXyFY4BGuN+EE0+GeR201b+wkkLN5mmBY5TfMw8ngqL</span></div><div class='line' id='LC2068'><span class="s">CztXxCSXKMCYrRIElWkEJlEPYsSOeKBVZCAQTKBhApMwRFQzmCThE0YQu2CdEhgjbgmk9GluHpfR</span></div><div class='line' id='LC2069'><span class="s">/hhwJCZhGI5jt5FsAkOrObVyE6g2y1snyhMGFlDY1x+BoHpCMulTj5JYWNAYJmnKpvLxXgmQ8az1</span></div><div class='line' id='LC2070'><span class="s">4fUGxxcitMbbhDFcsiAItg04E+OSBIHTUYD1HI4FHH4kMREPknuYRMyhh3AARWMkfhCketqD1CWJ</span></div><div class='line' id='LC2071'><span class="s">mTCo/nhUScoQcInB1hpFhIKoIXLo5jLpwFCgsnLCx1QlEMlz/iFEGqzH3vWYcpRcThgWnEKm0QcS</span></div><div class='line' id='LC2072'><span class="s">rA8ek2a2IYYeowUanOZOlrbWSJUC4c7y2EMI3uJPMnMF/SSXdk6E495VLhzkWHps0rOhKwqk+xBI</span></div><div class='line' id='LC2073'><span class="s">DhJirhdUCTamMfXz2Hy303hM4DFJ8QL21BcPBULR+gcdYxoeiDqOFSqpi5B5PUISfGg46gFZBPo4</span></div><div class='line' id='LC2074'><span class="s">jdh8lueaWuVSMTURfbAUnLINr/QYuuYoMQV6l1aWxuZVTjlaLC14UzqZ+ziTGDzJzhiYoPLrt3uI</span></div><div class='line' id='LC2075'><span class="s">tXkVR47kAo09lo5BD76CH51cTt1snVpMOttLhY93yxChCQPI4OBecS7++h4p4Bdn4H97bJongtPk</span></div><div class='line' id='LC2076'><span class="s">s9gQnXku1vzsjjmX4/o4YUDkXkjHwDg5FXozU0fW4y5kyeYW0uJWlh536BKr0kMGjtzTkng6Ep62</span></div><div class='line' id='LC2077'><span class="s">uTWnQtiIqKnEsx7e1hLtzlXs7Upw9TwEnp0t9yzCGgUJIZConx9OHJArLkRYW0dW42G9OeR5Nzwk</span></div><div class='line' id='LC2078'><span class="s">yk1mX7du5RGHT7dka7N3AznmSif7y6tuKe2N1Al/1TUPRqH6E2GLVc27h9IptMLkCKQYRqPQJgzV</span></div><div class='line' id='LC2079'><span class="s">2m6WLsSipS3v3b1/WmXEYY1meLEVIU/arOGVkyie7ZsH05ZKpjFW4cpY0YkjySpSExNG2TS8nnJx</span></div><div class='line' id='LC2080'><span class="s">nrQmWh2WY3cP1eISP9wbaVK35ZXc60yC3VN/j9n7UFoK6zvjSTE2+Pvz6Mx322rnftfP8Y0XKIdv</span></div><div class='line' id='LC2081'><span class="s">Qd7AfK0nexBTMqRiErvCMa3Hegpfjdh58glW2oNMsKeAX8x6YJLZs9K8/ozjJkWL+JmECMvhQ54x</span></div><div class='line' id='LC2082'><span class="s">9rsTHwcoGrDi6Y4I+H7yY4/rJVPAbYymUH7C2D3uiUS3KQ1nrCAUkE1dJMneDQIJMQQx5SONxoEO</span></div><div class='line' id='LC2083'><span class="s">OEn1/Ig1eBBUeEDRuOT2WGGGE4bNypBLFh2PeIg3bEbg44PHiqNDbGIQm50LW6MJU62JHCGBrmc9</span></div><div class='line' id='LC2084'><span class="s">2F7WBJrrj1ssnTAK4sxwRgh5LLblhwNAclv3Gd+jC/etCfyfR8TMhcWQz8TBIbG8IIyAQ81w2n/C</span></div><div class='line' id='LC2085'><span class="s">mHWAwRzxd3WoBY7BZnsqGOWrOCKwGkMMNfO0Kci/joZgEocLjNnzgcmdehPHJY0FudXgsr+v44TB</span></div><div class='line' id='LC2086'><span class="s">I3jnMGnsK5veAhgi9iXGifkHMOC09Rh9cAw9sQ0asl6wKMk8mpzFYaaDSgG4F0wisQDDBRpjCINg</span></div><div class='line' id='LC2087'><span class="s">FIxhlhQ31xdSkkk6odXZFpTYOQpOOgw9ugM2cDQ+2MYa7JsEirGBrOuxsQy5nPMRdYjsTJ/j1iNw</span></div><div class='line' id='LC2088'><span class="s">FeSt1jY2+dd5yx1/pzZMOQXUIDcXeAzR7QlDRM8AMkUldXOmGmvYXPABjxqkYKO7VAY6JRU7kpXr</span></div><div class='line' id='LC2089'><span class="s">+Epu2BU3qFFXClFi27784LrDZsJwbNlDw0JzhZ6M0SMXE4iBHehCpHVkrQhpTFn2dsvsZYkiPEEB</span></div><div class='line' id='LC2090'><span class="s">GSEAwdiur9LS1U6P2U9JhGp4hnFpJo4FfkdJHcwV6Q5dV1Q9uNeeu7rV8PAjwdFg9RLtroifOr0k</span></div><div class='line' id='LC2091'><span class="s">uOiRTo/obNPhQIf42Fr4mtThWoSjitEdAmFW66UCe8WFjPk1YVNpL9srFbond7jrLg8tqAasIMpy</span></div><div class='line' id='LC2092'><span class="s">zkH0SY/6zVAwJrEc14zt14YRXdY+fcJ4qOd2XKB0/Kghw1ovd11t2o+zjt+txndo1ZDZ2T+uMVHT</span></div><div class='line' id='LC2093'><span class="s">VSXhedBAHoJIID9xm6wPQI3cXY+HR7vxtrJuCKh6kbXaW5KkVeJsdsjqsYsOwYSh0w5sMbu7LF8J</span></div><div class='line' id='LC2094'><span class="s">5T7U6LJdiTx+ca7RKlulGgS5Z1JSU2Llt32cHFipkaurtBrvNX5UtvNZjkufZ/r1/XyLl6yOpytL</span></div><div class='line' id='LC2095'><span class="s">Km8Fn+y4wkhlqZP5db0rooqy7xdL4wxzFVTX+6HaxuQJK5E5B1neSSovZ9ALB8091dDbbjVxhWNY</span></div><div class='line' id='LC2096'><span class="s">Ve5hn1VnI9OF0wpvaRm7SZuC1IRczwC7GnkhPt3muHV1YxUJfo+uh1sYnJy+vI0ZwuPV2uqWJYUH</span></div><div class='line' id='LC2097'><span class="s">bmBsi1zmFSxHrqwA+WIzLrHkwW4r+bad7xbOzJCnKIa3S3YvrzEBK1Dc0emzJW+SqysQfdEDorQG</span></div><div class='line' id='LC2098'><span class="s">9ZJlbQzEHQV8naPaF440YXzJk/7vHGK2xwuP+Gc5xITxyiP+WQ4x18oXHjFzCBy9kir1EFTAm0Zq</span></div><div class='line' id='LC2099'><span class="s">LYwS8MpiGhtfxiBRDXpxDWxk9g9Q2fzPPAhS6VFDAc/aiNGatUkPtZIStZFQ1qD0IlJa/5ZPAi5J</span></div><div class='line' id='LC2100'><span class="s">ySp1ETDomZMnvgiysZSBfMikrSDte/K5lqV6iwC5q7YN9I1dBZXUytDJNqU74MJsUyNNLAPopWK3</span></div><div class='line' id='LC2101'><span class="s">tzmLkCiDyl7WQnj9sm7Kd5kzgpoccdNeMw/6zPVB3pUwMgi4C7hj4AMFAf4G27oXH8NNT9zll/sK</span></div><div class='line' id='LC2102'><span class="s">S6wVlQwazjxWKWy20ZzXb9ne8ngGalPBWSUSj9xkc1drsXkZ8oOyvYT3e0rnYsGwx85xZB9wKeKg</span></div><div class='line' id='LC2103'><span class="s">cJKZnamYwiaMymZvzk6wtDUkxmdUg0mPad0YHtvzpjEfp2iMxvORhnx0kCVLf5Qa43WJsVoyfEyI</span></div><div class='line' id='LC2104'><span class="s">pzmf8ruM6xBr7dnBgzyxpqXuUPYaKahOaz1LrxNkS/Q3Ae5AC+xl6NbxAqXXlzghZBZHmOrM6Y6Y</span></div><div class='line' id='LC2105'><span class="s">ctAkltwlF7SKEsShjVh7QHuxMU0a08/eiu3x3M+07OijMcKFFltByXrpk8w+JNnZpnp3CfgjV1Ax</span></div><div class='line' id='LC2106'><span class="s">gUYCnWwYow42I5wHCcTzLXK0hMZN2DrPM/zCSqe9jRSlJnr70BPE4+zrwbk/xVIDHy2FAQyHoomT</span></div><div class='line' id='LC2107'><span class="s">Tt5jiM68nBQut35Y0qLclLiQrutxt/c0OlSqXAC8VrxW97lGoRWzhOnifE2zbF05W4xuyhg7JTUL</span></div><div class='line' id='LC2108'><span class="s">aqJ7SWDywhjlal0b+NLTpERBgnPW0+Nw99X2Ws72gOL27iER9jgzj7Uu09JaZ3n+hmCjjvZpjNst</span></div><div class='line' id='LC2109'><span class="s">vOWWTbuLrg+/1ltX8WpPauEDEvcunIgTxuMEHweWKCx2KQ9DU/UKdO/3za4Szm2iHYL+ss9AAttm</span></div><div class='line' id='LC2110'><span class="s">gZHq2pkUXFbV+FiJCKrpBms18zH75vax5jSo7FNunrVWY3Chvd8KKnHdaTt/6ealwaA1x17yTlft</span></div><div class='line' id='LC2111'><span class="s">8VBle3nAE+7R0MScC3MJofNCCkA9PGKBgGMYEwfB2QO5j8zUqa8F/EkWKCzGQJ5EZ05HTly1B01E</span></div><div class='line' id='LC2112'><span class="s">z813G5BY++RZ2sxbQS8ZveGPJNabp5kXAeoign6Tlt5+L8i5ZquY9+S+KEUHkmYMRFBxRrHnbl2X</span></div><div class='line' id='LC2113'><span class="s">rVemKnG+oB1yd9+zT+4c43jQ0wWmQRR6mTCkY1q3VG05Y120ZzKOMBe6Vy7I5Vz4ygPB3yY4G0FP</span></div><div class='line' id='LC2114'><span class="s">8RxiMx985YJPXsgRU58EuHj75gygTzejP+W/zKGe78UQN3yOJ1aMQV9hFH+GAfLRsza84WlPLAI/</span></div><div class='line' id='LC2115'><span class="s">9G/5JdcHftEfH+Y3/fHUG7/o8bv98dzzy3e8S+XCvgqB+VUf7sH0yDHpONdbRE8tAg9NWOzcTJ7q</span></div><div class='line' id='LC2116'><span class="s">TuAxe/AJ07c1Rs9okJvl1/0G60qvbdDzz5zO0FuPFQIHNp9y9Bd1CufYVx7dB26mAxwa8GMNrN/U</span></div><div class='line' id='LC2117'><span class="s">oGbNZ3EQ7inLzHy5tRg9AXJrN8cB59cCUBeCiVO7zKM0jU0MamhnRThkg/NMmBOGb6StNeD9tDfA</span></div><div class='line' id='LC2118'><span class="s">7czsAWopDdnGoXUHtA+s/k0vNPkBcxEI13jVd/axp85va3LpwGggXXWw12Gwr/JGAH0b8CPboiZd</span></div><div class='line' id='LC2119'><span class="s">QO1l0mk/UHukud4C+w5uRoNzpCmoW6GbgbMyaQNkga2pQINB18lOXOCJzSWPFOhZcwzdgrsQnne7</span></div><div class='line' id='LC2120'><span class="s">nvjBi+7cP2BbtBeDOW5uOLGf3z94FasKIguOqJl+8ss/6Kumns4cuWbqq5592TN/RNIbn5Qo6qbi</span></div><div class='line' id='LC2121'><span class="s">O4F0P9txxPAwagqPlftztO8cWBzdN/jz3b7GD6JHYP/Zp4ToAMaA74M+EGSft3hEGMuf8EwjnTk/</span></div><div class='line' id='LC2122'><span class="s">nz/P7SLipB/ogQ6xNX0fDqNncMCfHqGLCMM0ZzFa+6lPJYQ5p81vW4HkCvidYf6kb+P/oB965g8K</span></div><div class='line' id='LC2123'><span class="s">C6uR0rdjX1DNKc5pOSTquI8uQ6KXxYaKBn+30/09tK4kMpJPgUIQkbENEPbuezNPPje2Um83SgyX</span></div><div class='line' id='LC2124'><span class="s">GTCJb6MnGVIpgncdQg1qz2bvPfxYD9fewCXDomx9S+HQJuX6W3VAL+v5WZMudRQZk9ZdOk6GIUtC</span></div><div class='line' id='LC2125'><span class="s">PqEb/uwSIrtR7/edzqgEdtpEwq7p2J5OQV+RLrmtTvFwFpf03M/VrRyTZ73qVod7v7Jh2Dwe5J25</span></div><div class='line' id='LC2126'><span class="s">JqFOU2qEu1sP+CRotklediycKfLjeIZzjJQsvKmiGSNQhxuJpKa+hoWUizaE1PuIRGzJqropwgVB</span></div><div class='line' id='LC2127'><span class="s">oo1hr870MZLgnXF5ZIpr6mF0L8aSy2gVnTAuoB4WEd4d5NPVC9TMotYXERKlTcwQ2KiB/C48AEfH</span></div><div class='line' id='LC2128'><span class="s">Qbyq4CN8xTFnTvf/ebOc3isnjD95s0QF0nx9s+y+zMmz782xL0SgEmRpA3x1w1Ff9/74xcxKEPdS</span></div><div class='line' id='LC2129'><span class="s">IEFTz6GgU0+BK/UZ5Gwbl4gZwycxEw+Kqa5QmMkh4OzgzEVPnDAiAOGBFaBW4wkDmj1G4RyElKgj</span></div><div class='line' id='LC2130'><span class="s">NlLCq8zsp085MNh/+R4t1Q8yxoSv8PUpTt7izZwf2BTHZZ3pIZpUIpuLkL1nNL6sYcHqcKm237wp</span></div><div class='line' id='LC2131'><span class="s">T2+RCjgXweXd2Zp7ZM8W6dG5bZsqo0nrJBTx8EC0+CQQdzEGnabTnkzofu1pYkWl4E7XSniECdxy</span></div><div class='line' id='LC2132'><span class="s">vLYavPMcL9LW5SToJFNnos+uqweOHriUZ1ntIYZUonc7ltEQ6oTRtwOHNwez2sVREskHN+bqG3ua</span></div><div class='line' id='LC2133'><span class="s">eaEbJ8XpyO8CeD9QJc8nbLP2C2R3A437ISUNyt5Yd0TbDNcl11/DSsOzdbi/VhCC0KE6v1vqVNkq</span></div><div class='line' id='LC2134'><span class="s">45ZnG6fiV2NwzInxCNth3BwL0+8814jE6+1W1EeWtpWbSZJOJNYXmWRXa7vLnAljE692eHjZ4y5u</span></div><div class='line' id='LC2135'><span class="s">y1u63De0IzKca7As48Z3XshVF+3XiLNz0JIMh/JOpbiNLlMi672uO0wYzOCZjRxcxj3D+gVenGIE</span></div><div class='line' id='LC2136'><span class="s">MvFUGGXuRps2RzMcgWIRolHXpGUP6sMsQt1hspUBnVKUn/WQj2u6j3SXd9Xz0QtEzoM7qTu5y7gR</span></div><div class='line' id='LC2137'><span class="s">q9gNNsrlEMLdikBt9bFvBnfbUIh6voTw7eDsyTmPKUvF0bHqWLbHe3VRHyRZnNeSGKsB73q66Vsk</span></div><div class='line' id='LC2138'><span class="s">taxWYmwz1tYVFG/vOQhlM0gUkyvIab3nv2caJ1udU1F3pDMty7stubTE4OJqm0i0ECfrJIkLtraC</span></div><div class='line' id='LC2139'><span class="s">HwRWKzlqpfhEIqYH09eT9WrOhQyt8YEoyBlnXtAT37WHIQ03TIuEHbnRxZDdLun0iok9PUC79prU</span></div><div class='line' id='LC2140'><span class="s">m5beZzfQUelEXnhzb/pIROKx3F7qCttYIFGh5dXNzFzID7u8vKykA8Uejf7XXz//S4nKvW//ofS/</span></div><div class='line' id='LC2141'><span class="s">QastYw==</span></div><div class='line' id='LC2142'><span class="s">&quot;&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC2143'><br/></div><div class='line' id='LC2144'><span class="c">##file distutils-init.py</span></div><div class='line' id='LC2145'><span class="n">DISTUTILS_INIT</span> <span class="o">=</span> <span class="n">convert</span><span class="p">(</span><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC2146'><span class="s">eJytV1uL4zYUfvevOE0ottuMW9q3gVDa3aUMXXbLMlDKMBiNrSTqOJKRlMxkf33PkXyRbGe7Dw2E</span></div><div class='line' id='LC2147'><span class="s">UXTu37lpxLFV2oIyifAncxmOL0xLIfcG+gv80x9VW6maw7o/CANSWWBwFtqeWMPlGY6qPjV8A0bB</span></div><div class='line' id='LC2148'><span class="s">C4eKSTgZ5LRgFeyErMEeOBhbN+Ipgeizhjtnhkn7DdyjuNLPoCS0l/ayQTG0djwZC08cLXozeMss</span></div><div class='line' id='LC2149'><span class="s">aG5EzQ0IScpnWtHSTXuxByV/QCmxE7y+eS0uxWeoheaVVfqSJHiU7Mhhi6gULbOHorshkrEnKxpT</span></div><div class='line' id='LC2150'><span class="s">0n3A8Y8SMpuwZx6aoix3ouFlmW8gHRSkeSJ2g7hU+kiHLDaQw3bmRDaTGfTnty7gPm0FHbIBg9U9</span></div><div class='line' id='LC2151'><span class="s">oh1kZzAFLaue2R6htPCtAda2nGlDSUJ4PZBgCJBGVcwKTAMz/vJiLD+Oin5Z5QlvDPdulC6EsiyE</span></div><div class='line' id='LC2152'><span class="s">NFzb7McNTKJzbJqzphx92VKRFY1idenzmq3K0emRcbWBD0ryqc4NZGmKOOOX9Pz5x+/l27tP797c</span></div><div class='line' id='LC2153'><span class="s">f/z0d+4NruGNai8uAM0bfsYaw8itFk8ny41jsfpyO+BWlpqfhcG4yxLdi/0tQqoT4a8Vby382mt8</span></div><div class='line' id='LC2154'><span class="s">p7XSo7aWGdPBc+b6utaBmCQ7rQKQoWtAuthQCiold2KfJIPTT8xwg9blPumc+YDZC/wYGdAyHpJk</span></div><div class='line' id='LC2155'><span class="s">vUbHbHWAp5No6pK/WhhLEWrFjUwtPEv1Agf8YmnsuXUQYkeZoHm8ogP16gt2uHoxcEMdf2C6pmbw</span></div><div class='line' id='LC2156'><span class="s">hUMsWGhanboh4IzzmsIpWs134jVPqD/c74bZHdY69UKKSn/+KfVhxLgUlToemayLMYQOqfEC61bh</span></div><div class='line' id='LC2157'><span class="s">cbhwaqoGUzIyZRFHPmau5juaWqwRn3mpWmoEA5nhzS5gog/5jbcFQqOZvmBasZtwYlG93k5GEiyw</span></div><div class='line' id='LC2158'><span class="s">buHhMWLjDarEGpMGB2LFs5nIJkhp/nUmZneFaRth++lieJtHepIvKgx6PJqIlD9X2j6pG1i9x3pZ</span></div><div class='line' id='LC2159'><span class="s">5bHuCPFiirGHeO7McvoXkz786GaKVzC9DSpnOxJdc4xm6NSVq7lNEnKdVlnpu9BNYoKX2Iq3wvgh</span></div><div class='line' id='LC2160'><span class="s">gGEUM66kK6j4NiyoneuPLSwaCWDxczgaolEWpiMyDVDb7dNuLAbriL8ig8mmeju31oNvQdpnvEPC</span></div><div class='line' id='LC2161'><span class="s">1vAXbWacGRVrGt/uXN/gU0CDDwgooKRrHfTBb1/s9lYZ8ZqOBU0yLvpuP6+K9hLFsvIjeNhBi0KL</span></div><div class='line' id='LC2162'><span class="s">MlOuWRn3FRwx5oHXjl0YImUx0+gLzjGchrgzca026ETmYJzPD+IpuKzNi8AFn048Thd63OdD86M6</span></div><div class='line' id='LC2163'><span class="s">84zE8yQm0VqXdbbgvub2pKVnS76icBGdeTHHXTKspUmr4NYo/furFLKiMdQzFjHJNcdAnMhltBJK</span></div><div class='line' id='LC2164'><span class="s">0/IKX3DVFqvPJ2dLE7bDBkH0l/PJ29074+F0CsGYOxsb7U3myTUncYfXqnLLfa6sJybX4g+hmcjO</span></div><div class='line' id='LC2165'><span class="s">kMRBfA1JellfRRKJcyRpxdS4rIl6FdmQCWjo/o9Qz7yKffoP4JHjOvABcRn4CZIT2RH4jnxmfpVG</span></div><div class='line' id='LC2166'><span class="s">qgLaAvQBNfuO6X0/Ux02nb4FKx3vgP+XnkX0QW9pLy/NsXgdN24dD3LxO2Nwil7Zlc1dqtP3d7/h</span></div><div class='line' id='LC2167'><span class="s">kzp1/+7hGBuY4pk0XD/0Ao/oTe/XGrfyM773aB7iUhgkpy+dwAMalxMP0DrBcsVw/6p25+/hobP9</span></div><div class='line' id='LC2168'><span class="s">GBknrWExDhLJ1bwt1NcCNblaFbMKCyvmX0PeRaQ=</span></div><div class='line' id='LC2169'><span class="s">&quot;&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC2170'><br/></div><div class='line' id='LC2171'><span class="c">##file distutils.cfg</span></div><div class='line' id='LC2172'><span class="n">DISTUTILS_CFG</span> <span class="o">=</span> <span class="n">convert</span><span class="p">(</span><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC2173'><span class="s">eJxNj00KwkAMhfc9xYNuxe4Ft57AjYiUtDO1wXSmNJnK3N5pdSEEAu8nH6lxHVlRhtDHMPATA4uH</span></div><div class='line' id='LC2174'><span class="s">xJ4EFmGbvfJiicSHFRzUSISMY6hq3GLCRLnIvSTnEefN0FIjw5tF0Hkk9Q5dRunBsVoyFi24aaLg</span></div><div class='line' id='LC2175'><span class="s">9FDOlL0FPGluf4QjcInLlxd6f6rqkgPu/5nHLg0cXCscXoozRrP51DRT3j9QNl99AP53T2Q=</span></div><div class='line' id='LC2176'><span class="s">&quot;&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC2177'><br/></div><div class='line' id='LC2178'><span class="c">##file activate_this.py</span></div><div class='line' id='LC2179'><span class="n">ACTIVATE_THIS</span> <span class="o">=</span> <span class="n">convert</span><span class="p">(</span><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC2180'><span class="s">eJyNU01v2zAMvetXEB4K21jmDOstQA4dMGCHbeihlyEIDMWmG62yJEiKE//7kXKdpN2KzYBt8euR</span></div><div class='line' id='LC2181'><span class="s">fKSyLPs8wiEo8wh4wqZTGou4V6Hm0wJa1cSiTkJdr8+GsoTRHuCotBayiWqQEYGtMCgfD1KjGYBe</span></div><div class='line' id='LC2182'><span class="s">5a3p0cRKiAe2NtLADikftnDco0ko/SFEVgEZ8aRC5GLux7i3BpSJ6J1H+i7A2CjiHq9z7JRZuuQq</span></div><div class='line' id='LC2183'><span class="s">siwTIvpxJYCeuWaBpwZdhB+yxy/eWz+ZvVSU8C4E9FFZkyxFsvCT/ZzL8gcz9aXVE14Yyp2M+2W0</span></div><div class='line' id='LC2184'><span class="s">y7n5mp0qN+avKXvbsyyzUqjeWR8hjGE+2iCE1W1tQ82hsCZN9UzlJr+/e/iab8WfqsmPI6pWeUPd</span></div><div class='line' id='LC2185'><span class="s">FrMsd4H/55poeO9n54COhUs+sZNEzNtg/wanpjpuqHJaxs76HtZryI/K3H7KJ/KDIhqcbJ7kI4ar</span></div><div class='line' id='LC2186'><span class="s">XL+sMgXnX0D+Te2Iy5xdP8yueSlQB/x/ED2BTAtyE3K4SYUN6AMNfbO63f4lBW3bUJPbTL+mjSxS</span></div><div class='line' id='LC2187'><span class="s">PyRfJkZRgj+VbFv+EzHFi5pKwUEepa4JslMnwkowSRCXI+m5XvEOvtuBrxHdhLalG0JofYBok6qj</span></div><div class='line' id='LC2188'><span class="s">YdN2dEngUlbC4PG60M1WEN0piu7Nq7on0mgyyUw3iV1etLo6r/81biWdQ9MWHFaePWZYaq+nmp+t</span></div><div class='line' id='LC2189'><span class="s">s3az+sj7eA0jfgPfeoN1</span></div><div class='line' id='LC2190'><span class="s">&quot;&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC2191'><br/></div><div class='line' id='LC2192'><span class="n">MH_MAGIC</span> <span class="o">=</span> <span class="mh">0xfeedface</span></div><div class='line' id='LC2193'><span class="n">MH_CIGAM</span> <span class="o">=</span> <span class="mh">0xcefaedfe</span></div><div class='line' id='LC2194'><span class="n">MH_MAGIC_64</span> <span class="o">=</span> <span class="mh">0xfeedfacf</span></div><div class='line' id='LC2195'><span class="n">MH_CIGAM_64</span> <span class="o">=</span> <span class="mh">0xcffaedfe</span></div><div class='line' id='LC2196'><span class="n">FAT_MAGIC</span> <span class="o">=</span> <span class="mh">0xcafebabe</span></div><div class='line' id='LC2197'><span class="n">BIG_ENDIAN</span> <span class="o">=</span> <span class="s">&#39;&gt;&#39;</span></div><div class='line' id='LC2198'><span class="n">LITTLE_ENDIAN</span> <span class="o">=</span> <span class="s">&#39;&lt;&#39;</span></div><div class='line' id='LC2199'><span class="n">LC_LOAD_DYLIB</span> <span class="o">=</span> <span class="mh">0xc</span></div><div class='line' id='LC2200'><span class="n">maxint</span> <span class="o">=</span> <span class="n">majver</span> <span class="o">==</span> <span class="mi">3</span> <span class="ow">and</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">sys</span><span class="p">,</span> <span class="s">&#39;maxsize&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">sys</span><span class="p">,</span> <span class="s">&#39;maxint&#39;</span><span class="p">)</span></div><div class='line' id='LC2201'><br/></div><div class='line' id='LC2202'><br/></div><div class='line' id='LC2203'><span class="k">class</span> <span class="nc">fileview</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC2204'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC2205'><span class="sd">    A proxy for file-like objects that exposes a given view of a file.</span></div><div class='line' id='LC2206'><span class="sd">    Modified from macholib.</span></div><div class='line' id='LC2207'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC2208'><br/></div><div class='line' id='LC2209'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fileobj</span><span class="p">,</span> <span class="n">start</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="n">maxint</span><span class="p">):</span></div><div class='line' id='LC2210'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">fileobj</span><span class="p">,</span> <span class="n">fileview</span><span class="p">):</span></div><div class='line' id='LC2211'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_fileobj</span> <span class="o">=</span> <span class="n">fileobj</span><span class="o">.</span><span class="n">_fileobj</span></div><div class='line' id='LC2212'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC2213'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_fileobj</span> <span class="o">=</span> <span class="n">fileobj</span></div><div class='line' id='LC2214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_start</span> <span class="o">=</span> <span class="n">start</span></div><div class='line' id='LC2215'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_end</span> <span class="o">=</span> <span class="n">start</span> <span class="o">+</span> <span class="n">size</span></div><div class='line' id='LC2216'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_pos</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC2217'><br/></div><div class='line' id='LC2218'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC2219'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;&lt;fileview [</span><span class="si">%d</span><span class="s">, </span><span class="si">%d</span><span class="s">] </span><span class="si">%r</span><span class="s">&gt;&#39;</span> <span class="o">%</span> <span class="p">(</span></div><div class='line' id='LC2220'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_start</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fileobj</span><span class="p">)</span></div><div class='line' id='LC2221'><br/></div><div class='line' id='LC2222'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">tell</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC2223'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pos</span></div><div class='line' id='LC2224'><br/></div><div class='line' id='LC2225'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_checkwindow</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">seekto</span><span class="p">,</span> <span class="n">op</span><span class="p">):</span></div><div class='line' id='LC2226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_start</span> <span class="o">&lt;=</span> <span class="n">seekto</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end</span><span class="p">):</span></div><div class='line' id='LC2227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">IOError</span><span class="p">(</span><span class="s">&quot;</span><span class="si">%s</span><span class="s"> to offset </span><span class="si">%d</span><span class="s"> is outside window [</span><span class="si">%d</span><span class="s">, </span><span class="si">%d</span><span class="s">]&quot;</span> <span class="o">%</span> <span class="p">(</span></div><div class='line' id='LC2228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">op</span><span class="p">,</span> <span class="n">seekto</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end</span><span class="p">))</span></div><div class='line' id='LC2229'><br/></div><div class='line' id='LC2230'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">seek</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">whence</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></div><div class='line' id='LC2231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seekto</span> <span class="o">=</span> <span class="n">offset</span></div><div class='line' id='LC2232'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">whence</span> <span class="o">==</span> <span class="n">os</span><span class="o">.</span><span class="n">SEEK_SET</span><span class="p">:</span></div><div class='line' id='LC2233'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seekto</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start</span></div><div class='line' id='LC2234'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">whence</span> <span class="o">==</span> <span class="n">os</span><span class="o">.</span><span class="n">SEEK_CUR</span><span class="p">:</span></div><div class='line' id='LC2235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seekto</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pos</span></div><div class='line' id='LC2236'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">whence</span> <span class="o">==</span> <span class="n">os</span><span class="o">.</span><span class="n">SEEK_END</span><span class="p">:</span></div><div class='line' id='LC2237'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seekto</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end</span></div><div class='line' id='LC2238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC2239'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">IOError</span><span class="p">(</span><span class="s">&quot;Invalid whence argument to seek: </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">whence</span><span class="p">,))</span></div><div class='line' id='LC2240'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_checkwindow</span><span class="p">(</span><span class="n">seekto</span><span class="p">,</span> <span class="s">&#39;seek&#39;</span><span class="p">)</span></div><div class='line' id='LC2241'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_fileobj</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="n">seekto</span><span class="p">)</span></div><div class='line' id='LC2242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_pos</span> <span class="o">=</span> <span class="n">seekto</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start</span></div><div class='line' id='LC2243'><br/></div><div class='line' id='LC2244'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">):</span></div><div class='line' id='LC2245'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">here</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pos</span></div><div class='line' id='LC2246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_checkwindow</span><span class="p">(</span><span class="n">here</span><span class="p">,</span> <span class="s">&#39;write&#39;</span><span class="p">)</span></div><div class='line' id='LC2247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_checkwindow</span><span class="p">(</span><span class="n">here</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="nb">bytes</span><span class="p">),</span> <span class="s">&#39;write&#39;</span><span class="p">)</span></div><div class='line' id='LC2248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_fileobj</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="n">here</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">SEEK_SET</span><span class="p">)</span></div><div class='line' id='LC2249'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_fileobj</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">bytes</span><span class="p">)</span></div><div class='line' id='LC2250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_pos</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="nb">bytes</span><span class="p">)</span></div><div class='line' id='LC2251'><br/></div><div class='line' id='LC2252'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="n">maxint</span><span class="p">):</span></div><div class='line' id='LC2253'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">size</span> <span class="o">&gt;=</span> <span class="mi">0</span></div><div class='line' id='LC2254'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">here</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pos</span></div><div class='line' id='LC2255'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_checkwindow</span><span class="p">(</span><span class="n">here</span><span class="p">,</span> <span class="s">&#39;read&#39;</span><span class="p">)</span></div><div class='line' id='LC2256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">size</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">size</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end</span> <span class="o">-</span> <span class="n">here</span><span class="p">)</span></div><div class='line' id='LC2257'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_fileobj</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="n">here</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">SEEK_SET</span><span class="p">)</span></div><div class='line' id='LC2258'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">bytes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fileobj</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="n">size</span><span class="p">)</span></div><div class='line' id='LC2259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_pos</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="nb">bytes</span><span class="p">)</span></div><div class='line' id='LC2260'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bytes</span></div><div class='line' id='LC2261'><br/></div><div class='line' id='LC2262'><br/></div><div class='line' id='LC2263'><span class="k">def</span> <span class="nf">read_data</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">endian</span><span class="p">,</span> <span class="n">num</span><span class="o">=</span><span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC2264'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC2265'><span class="sd">    Read a given number of 32-bits unsigned integers from the given file</span></div><div class='line' id='LC2266'><span class="sd">    with the given endianness.</span></div><div class='line' id='LC2267'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC2268'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">res</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="n">endian</span> <span class="o">+</span> <span class="s">&#39;L&#39;</span> <span class="o">*</span> <span class="n">num</span><span class="p">,</span> <span class="nb">file</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="n">num</span> <span class="o">*</span> <span class="mi">4</span><span class="p">))</span></div><div class='line' id='LC2269'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">res</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC2270'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">res</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC2271'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">res</span></div><div class='line' id='LC2272'><br/></div><div class='line' id='LC2273'><br/></div><div class='line' id='LC2274'><span class="k">def</span> <span class="nf">mach_o_change</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">what</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span></div><div class='line' id='LC2275'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC2276'><span class="sd">    Replace a given name (what) in any LC_LOAD_DYLIB command found in</span></div><div class='line' id='LC2277'><span class="sd">    the given binary with a new name (value), provided it&#39;s shorter.</span></div><div class='line' id='LC2278'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC2279'><br/></div><div class='line' id='LC2280'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">do_macho</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">bits</span><span class="p">,</span> <span class="n">endian</span><span class="p">):</span></div><div class='line' id='LC2281'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Read Mach-O header (the magic number is assumed read by the caller)</span></div><div class='line' id='LC2282'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cputype</span><span class="p">,</span> <span class="n">cpusubtype</span><span class="p">,</span> <span class="n">filetype</span><span class="p">,</span> <span class="n">ncmds</span><span class="p">,</span> <span class="n">sizeofcmds</span><span class="p">,</span> <span class="n">flags</span> <span class="o">=</span> <span class="n">read_data</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">endian</span><span class="p">,</span> <span class="mi">6</span><span class="p">)</span></div><div class='line' id='LC2283'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># 64-bits header has one more field.</span></div><div class='line' id='LC2284'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">bits</span> <span class="o">==</span> <span class="mi">64</span><span class="p">:</span></div><div class='line' id='LC2285'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">read_data</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">endian</span><span class="p">)</span></div><div class='line' id='LC2286'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># The header is followed by ncmds commands</span></div><div class='line' id='LC2287'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">ncmds</span><span class="p">):</span></div><div class='line' id='LC2288'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">where</span> <span class="o">=</span> <span class="nb">file</span><span class="o">.</span><span class="n">tell</span><span class="p">()</span></div><div class='line' id='LC2289'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Read command header</span></div><div class='line' id='LC2290'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cmd</span><span class="p">,</span> <span class="n">cmdsize</span> <span class="o">=</span> <span class="n">read_data</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">endian</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span></div><div class='line' id='LC2291'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">cmd</span> <span class="o">==</span> <span class="n">LC_LOAD_DYLIB</span><span class="p">:</span></div><div class='line' id='LC2292'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># The first data field in LC_LOAD_DYLIB commands is the</span></div><div class='line' id='LC2293'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># offset of the name, starting from the beginning of the</span></div><div class='line' id='LC2294'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># command.</span></div><div class='line' id='LC2295'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name_offset</span> <span class="o">=</span> <span class="n">read_data</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">endian</span><span class="p">)</span></div><div class='line' id='LC2296'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">file</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="n">where</span> <span class="o">+</span> <span class="n">name_offset</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">SEEK_SET</span><span class="p">)</span></div><div class='line' id='LC2297'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Read the NUL terminated string</span></div><div class='line' id='LC2298'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">load</span> <span class="o">=</span> <span class="nb">file</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="n">cmdsize</span> <span class="o">-</span> <span class="n">name_offset</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span></div><div class='line' id='LC2299'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">load</span> <span class="o">=</span> <span class="n">load</span><span class="p">[:</span><span class="n">load</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\0</span><span class="s">&#39;</span><span class="p">)]</span></div><div class='line' id='LC2300'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># If the string is what is being replaced, overwrite it.</span></div><div class='line' id='LC2301'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">load</span> <span class="o">==</span> <span class="n">what</span><span class="p">:</span></div><div class='line' id='LC2302'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">file</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="n">where</span> <span class="o">+</span> <span class="n">name_offset</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">SEEK_SET</span><span class="p">)</span></div><div class='line' id='LC2303'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">encode</span><span class="p">()</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\0</span><span class="s">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span></div><div class='line' id='LC2304'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Seek to the next command</span></div><div class='line' id='LC2305'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">file</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="n">where</span> <span class="o">+</span> <span class="n">cmdsize</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">SEEK_SET</span><span class="p">)</span></div><div class='line' id='LC2306'><br/></div><div class='line' id='LC2307'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">do_file</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">offset</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="n">maxint</span><span class="p">):</span></div><div class='line' id='LC2308'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">file</span> <span class="o">=</span> <span class="n">fileview</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">size</span><span class="p">)</span></div><div class='line' id='LC2309'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Read magic number</span></div><div class='line' id='LC2310'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">magic</span> <span class="o">=</span> <span class="n">read_data</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">BIG_ENDIAN</span><span class="p">)</span></div><div class='line' id='LC2311'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">magic</span> <span class="o">==</span> <span class="n">FAT_MAGIC</span><span class="p">:</span></div><div class='line' id='LC2312'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Fat binaries contain nfat_arch Mach-O binaries</span></div><div class='line' id='LC2313'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">nfat_arch</span> <span class="o">=</span> <span class="n">read_data</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">BIG_ENDIAN</span><span class="p">)</span></div><div class='line' id='LC2314'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">nfat_arch</span><span class="p">):</span></div><div class='line' id='LC2315'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Read arch header</span></div><div class='line' id='LC2316'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cputype</span><span class="p">,</span> <span class="n">cpusubtype</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">size</span><span class="p">,</span> <span class="n">align</span> <span class="o">=</span> <span class="n">read_data</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">BIG_ENDIAN</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span></div><div class='line' id='LC2317'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">do_file</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">size</span><span class="p">)</span></div><div class='line' id='LC2318'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">magic</span> <span class="o">==</span> <span class="n">MH_MAGIC</span><span class="p">:</span></div><div class='line' id='LC2319'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">do_macho</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="mi">32</span><span class="p">,</span> <span class="n">BIG_ENDIAN</span><span class="p">)</span></div><div class='line' id='LC2320'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">magic</span> <span class="o">==</span> <span class="n">MH_CIGAM</span><span class="p">:</span></div><div class='line' id='LC2321'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">do_macho</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="mi">32</span><span class="p">,</span> <span class="n">LITTLE_ENDIAN</span><span class="p">)</span></div><div class='line' id='LC2322'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">magic</span> <span class="o">==</span> <span class="n">MH_MAGIC_64</span><span class="p">:</span></div><div class='line' id='LC2323'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">do_macho</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="mi">64</span><span class="p">,</span> <span class="n">BIG_ENDIAN</span><span class="p">)</span></div><div class='line' id='LC2324'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">magic</span> <span class="o">==</span> <span class="n">MH_CIGAM_64</span><span class="p">:</span></div><div class='line' id='LC2325'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">do_macho</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="mi">64</span><span class="p">,</span> <span class="n">LITTLE_ENDIAN</span><span class="p">)</span></div><div class='line' id='LC2326'><br/></div><div class='line' id='LC2327'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">what</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="n">value</span><span class="p">))</span></div><div class='line' id='LC2328'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">do_file</span><span class="p">(</span><span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="s">&#39;r+b&#39;</span><span class="p">))</span></div><div class='line' id='LC2329'><br/></div><div class='line' id='LC2330'><br/></div><div class='line' id='LC2331'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></div><div class='line' id='LC2332'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">main</span><span class="p">()</span></div><div class='line' id='LC2333'><br/></div><div class='line' id='LC2334'><span class="c">## TODO:</span></div><div class='line' id='LC2335'><span class="c">## Copy python.exe.manifest</span></div><div class='line' id='LC2336'><span class="c">## Monkeypatch distutils.sysconfig</span></div></pre></div></td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.06926s from github-fe127-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/pypa/virtualenv/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close js-ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

  </body>
</html>

