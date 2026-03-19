

# console

Exposes the console API to Kotlin.

```kotlin
external val console: Console(source)
```

```kotlin
import kotlin.js.Console

external val console: Console

fun main() {
    console.log("Hello from Kotlin/JS!")
    console.warn("This is a warning")
    console.error("Something went wrong")
    console.info("Some info for you")
    console.dir(js("{ name: 'Kotlin', version: 1.9 }"))
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/console.html)

    