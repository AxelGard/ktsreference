

# hasSurrogatePairAt

Returns true if this CharSequence has Unicode surrogate pair at the specified index.

```kotlin
fun CharSequence.hasSurrogatePairAt(index: Int): Boolean(source)
```

```kotlin
val emoji = "👍"          // U+1F44D is represented by a surrogate pair
val index = 0            // first code unit of the string
println(emoji.hasSurrogatePairAt(index))   // prints: true
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/has-surrogate-pair-at.html)

    