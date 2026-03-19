

# associateBy

Returns a Map containing the characters from the given char sequence indexed by the key returned from keySelector function applied to each character.

```kotlin
inline fun <K> CharSequence.associateBy(keySelector: (Char) -> K): Map<K, Char>(source)
```

```kotlin
val text = "Kotlin"
val charMap: Map<Int, Char> = text.associateBy { it.code }

// Example output:
// {75=K, 111=o, 116=t, 108=l, 105=i, 110=n}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/associate-by.html)

    