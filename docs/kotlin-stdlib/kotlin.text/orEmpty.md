

# orEmpty

Returns the string if it is not null, or the empty string otherwise.

```kotlin
inline fun String?.orEmpty(): String(source)
```

```kotlin
val maybeName: String? = null
val name = maybeName.orEmpty()   // name == ""

val greeting = "Hello, ${maybeName.orEmpty()}!"
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/or-empty.html)

    