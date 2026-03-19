

# asDynamic

Reinterprets this value as a value of the /docs/reference/dynamic-type.html.

```kotlin
inline fun Any?.asDynamic(): dynamic(source)
```

```kotlin
import kotlin.js.*

fun main() {
    // JavaScript object received from somewhere (e.g., a library or a REST call)
    val jsObj: Any? = js("{ title: 'Kotlin', year: 2023 }")

    // Reinterpret it as a dynamic type
    val dyn = jsObj.asDynamic()

    // Read properties as you would in JavaScript
    console.log(dyn.title)   // -> Kotlin
    console.log(dyn.year)    // -> 2023

    // Modify a property
    dyn.year = 2024
    console.log(dyn.year)    // -> 2024
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/as-dynamic.html)

    