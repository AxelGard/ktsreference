

# definedExternally

The property that can be used as a placeholder for statements and values that are defined in JavaScript.

```kotlin
actual external val definedExternally: Nothing(source)
```

```kotlin
external interface Math {
    fun sqrt(value: Double): Double
}

val Math: Math = definedExternally

fun calculateSquareRoot(x: Double): Double = Math.sqrt(x)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/defined-externally.html)

    