

# toKotlinUuid

Converts this java.util.UUID value to the corresponding kotlin.uuid.Uuid value.

```kotlin
@ExperimentalUuidApiinline fun UUID.toKotlinUuid(): Uuid(source)
```

```kotlin
import java.util.UUID
import kotlin.uuid.ExperimentalUuidApi
import kotlin.uuid.Uuid
import kotlin.uuid.toKotlinUuid

@OptIn(ExperimentalUuidApi::class)
fun main() {
    val javaUuid: UUID = UUID.randomUUID()
    val kotlinUuid: Uuid = javaUuid.toKotlinUuid()

    println("Java UUID: $javaUuid")
    println("Kotlin Uuid: $kotlinUuid")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.uuid/to-kotlin-uuid.html)

    