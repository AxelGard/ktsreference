

# associateWith

Returns a Map where keys are characters from the given char sequence and values are produced by the valueSelector function applied to each character.

```kotlin
inline fun <V> CharSequence.associateWith(valueSelector: (Char) -> V): Map<Char, V>(source)
```

```kotlin
val charCodes = "hello".associateWith { it.code }
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/associate-with.html)

    