

# undefined

Exposes the JavaScript undefined property to Kotlin.

```kotlin
external val undefined: Nothing?(source)
```

```kotlin
import kotlin.js.*

fun main() {
    // `missing` holds the JavaScript undefined value
    val missing: dynamic = undefined
    println(missing === undefined)  // prints: true

    // Accessing a non‑existent property returns undefined
    val obj: dynamic = js("{ foo: 42 }")
    println(obj.bar === undefined)  // prints: true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/undefined.html)

    